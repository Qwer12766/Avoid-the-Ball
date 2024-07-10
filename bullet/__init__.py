import math
import pygame

from bullet.dataclasse 			import *
from bullet.dataset 			import *
from bullet.mainbulletclasse 	import BULLET, MultipleBullet


class Normal_Bullet(BULLET):
	def __init__(self,
				start_position	: Vector,
				contact_range 	: float,
				life_time 		: float,
				speed			: float,
				shadow_color	: Color,
					
				target_position	: Vector):
		
		BULLET.__init__(self, start_position, contact_range, life_time, speed)

		self.angle = self._targetAngle(target_position)
		self.shadow_color = shadow_color
		

	def Movement(self,
				screen 			: pygame.surface.Surface, _):
		
		self._NextPosition(self.angle)
		self.ShowBullet(screen, self.shadow_color, self.contact_range)

		return None
class Guided_Bullet(BULLET):	
	def __init__(self, 
		  		start_position	: Vector,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float,
				shadow_color	: Color,
				target_position	: Vector):
		
		BULLET.__init__(self, start_position, contact_range, life_time, speed)
		self.shadow_color = shadow_color

	def Movement(self,
			  	screen			: pygame.surface.Surface,
				target_position	: Vector,):
		
		self._NextPosition(self._targetAngle(target_position))
		self.ShowBullet(screen, self.shadow_color, self.contact_range)

		return None
class Variable_Velocity_Guided_Bullet(BULLET):	
	def __init__(self, 
		  		start_position	: Vector,
		  		contact_range 	: float,
		  		life_time 		: float,
				shadow_color	: Color,
				target_position	: Vector,

		  		max_speed		: float,
		  		min_speed		: float,
		  		attenuation_value:float):
		
		BULLET.__init__(self, start_position, contact_range, life_time, 0)

		self.max_speed   	 = max_speed
		self.min_speed   	 = min_speed
		self.attenuation_value= attenuation_value
		self.target_angle 	 = 0.0
		self.shadow_color = shadow_color

	def Movement(self, 
			  	screen 			: pygame.surface.Surface,
				target_position	: Vector):
		
		if self.speed < self.min_speed:
			self.target_angle= self._targetAngle(target_position)
			self.speed 	  	= self.max_speed

		self.speed *= 1-self.attenuation_value
		self._NextPosition(self.target_angle)

		self.ShowBullet(screen, self.shadow_color, self.contact_range)
		return None
class Normal_Multiple_Bullet(Normal_Bullet, MultipleBullet):
	def __init__(self,
			  	start_position	: Vector,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float,
				shadow_color	: Color,
				target_position	: Vector,

				shots_angle		: float,
				shots_size		: int,
				shots_cool_time : float,
				shots_spin_angle: float,

		  		shots_contact_range : float,
		  		shots_life_time 	: float,
		  		shots_speed			: float,
				shots_shadow_color	: Color,):
		  
		Normal_Bullet.__init__(self, 
						start_position, 
						contact_range, 
						life_time, 
						speed, 
						shadow_color,
						target_position)
		
		MultipleBullet.__init__(self, 
						start_position, 
						self.angle, 
						shots_angle, 
						shots_size, 
						shots_cool_time, 
						shots_spin_angle, 

						Normal_Bullet, 
						contact_range 	= shots_contact_range, 
						life_time 		= shots_life_time, 
						speed 			= shots_speed,
						shadow_color 	= shots_shadow_color)
		
	def Movement(self, 
			  	screen 			: pygame.surface.Surface, 
				target_position	: Vector):
		
		Normal_Bullet.Movement(self, screen, None)
		return MultipleBullet.Movement(self, self.position)

class Formation:
	def circle(
			range_ 			: float, 
			size 		  	: int,
			center_position	: Vector,
			target_position : Vector,
			bullat_type		: type,
			arc_angle		: float = 1) -> list:
		
		bullat_angle = 2*math.pi/size
	
		bullets = []
		
		for i in range(size):
			X_Pos = math.cos(bullat_angle*i*arc_angle)*range_ + center_position.x
			Y_Pos = math.sin(bullat_angle*i*arc_angle)*range_ + center_position.y
			
			bullets.append(
				bullat_type(**bulletsetting[bullat_type.__name__], target_position = target_position, start_position = Vector(X_Pos, Y_Pos)))
					
		return bullets
		
	def wall(
			range_ 			: float, 
			size 		  	: int,
			location	   	: Vector,
			center_position	: Vector,
			target_position : Vector,
			bullat_type		: type,
			target_centralization : bool = False) -> list:
				
		bullat_crack = range_/(size-0.999)*2
		
		bullets = []

		bulletsetting_ = {}
		bulletsetting_.update(bulletsetting[bullat_type.__name__])
				
		for i in range(size):
			if location[1] == 0:
				X_Pos = (range_ * location[0])
				Y_Pos = (bullat_crack*i) - range_
				
				if not target_centralization: target_position = Vector(-X_Pos + center_position.x, Y_Pos + center_position.y)
			else:
				X_Pos = (bullat_crack*i) - range_
				Y_Pos = (range_ * location[1])
				
				if not target_centralization: target_position = Vector(X_Pos + center_position.x, -Y_Pos + center_position.y)
			
			bullets.append(
				bullat_type(**bulletsetting_, target_position = target_position, start_position = Vector(X_Pos + center_position.x, Y_Pos + center_position.y)))
				
		return bullets
		

if __name__ == "__main__":
	import sys
	import random

	bullets = []

	pygame.init()
	size = [700, 700]
	screen = pygame.display.set_mode(size)

	clock = pygame.time.Clock()

	bullat_type = Normal_Bullet
	formation_ = Formation.circle
	
	GAME = True
	while GAME:
		MousePos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		StartPos = Vector(random.randint(0,size[0]), random.randint(0,size[1]))

		clock.tick(64) 

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()


			other = {'range_' : 350, 'size' : 8, 'center_position' : Vector(350,350), 'target_position' : MousePos}

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_u: bullat_type = Normal_Bullet
				if event.key == pygame.K_i: bullat_type = Guided_Bullet
				if event.key == pygame.K_o: bullat_type = Variable_Velocity_Guided_Bullet
				if event.key == pygame.K_p: bullat_type = Normal_Multiple_Bullet


				if event.key == pygame.K_RSHIFT: bullets += Formation.circle(bullat_type = bullat_type, **other)

				if event.key == pygame.K_UP: 	bullets += Formation.wall(bullat_type = bullat_type, location = Vector.Up, 		**other)
				if event.key == pygame.K_DOWN: 	bullets += Formation.wall(bullat_type = bullat_type, location = Vector.Down, 	**other)
				if event.key == pygame.K_RIGHT:	bullets += Formation.wall(bullat_type = bullat_type, location = Vector.Right, 	**other)
				if event.key == pygame.K_LEFT: 	bullets += Formation.wall(bullat_type = bullat_type, location = Vector.Left, 	**other)

				'''
				if event.key == pygame.K_UP:
					bullets += Formation.circle(range_ 		 	= 600,
												size 		   	= 8,
												center_position = MousePos,
												bullat_type 	= Guided_Bullet)
					
				if event.key == pygame.K_DOWN:
					bullets += Formation.circle(range_ 		 	= 700,
												size 		   	= 6,
												center_position = MousePos,
												bullat_type 	= Variable_Velocity_Guided_Bullet)

				if event.key == pygame.K_RIGHT:
					bullets += Formation.wall(range_ 		 	= 1000,
												size 		   	= 9,
												location		= Vector.Right,
												center_position = MousePos,
												bullat_type 	= Normal_Bullet,
												add_target  	= True)
					
				if event.key == pygame.K_LEFT:
					bullets += Formation.wall(range_ 		 	=1000,
												size 		   	= 4,
												location		= Vector.Left,
												center_position = MousePos,
												bullat_type 	= Normal_Multiple_Bullet,
												add_target  	= True)
				'''
				
		screen.fill(Color.white)

		for bullet in bullets:
			shots = bullet.Movement(screen, MousePos)
			if shots: bullets += shots
			
			Del_Checke = bullet.DelChecker(MousePos)
			
			if Del_Checke == 1: bullets.remove(bullet)
			elif Del_Checke == 2:
				#GAME = False
				print('GameOver')

		pygame.display.update()
		
	pygame.quit()
	#sys.exit()