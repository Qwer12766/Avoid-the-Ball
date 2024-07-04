import time
import math
import pygame

from dataclasse 		import *
from dataset 			import *
from mainbulletclasse 	import BULLET, MultipleBullet


class Normal_Bullet(BULLET):
	def __init__(self,
				start_position	: Vector,
				contact_range 	: float,
				life_time 		: float,
				speed			: float,
					
				taget_position	: Vector):
		
		BULLET.__init__(self, start_position, contact_range, life_time, speed)

		self.angle = self._TagetAngle(taget_position)
		

	def Movement(self,
				screen 			: pygame.surface.Surface, _) -> None:
		
		self._NextPosition(self.angle)
		self.ShowBullet(screen, self.contact_range)
class Guided_Bullet(BULLET):	
	def __init__(self, 
		  		start_position	: Vector,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float):
		
		BULLET.__init__(self, start_position, contact_range, life_time, speed)


	def Movement(self,
			  	screen			: pygame.surface.Surface,
				taget_position	: Vector,) -> None:
		
		self._NextPosition(self._TagetAngle(taget_position))
		self.ShowBullet(screen, self.contact_range)
class Variable_Velocity_Guided_Bullet(BULLET):	
	def __init__(self, 
		  		start_position	: Vector,
		  		contact_range 	: float,
		  		life_time 		: float,

		  		max_speed		: float,
		  		min_speed		: float,
		  		attenuation_value:float):
		
		BULLET.__init__(self, start_position, contact_range, life_time, 0)

		self.max_speed   	 = max_speed
		self.min_speed   	 = min_speed
		self.attenuation_value= attenuation_value
		self.taget_angle 	 = 0.0


	def Movement(self, 
			  	screen 			: pygame.surface.Surface,
				taget_position	: Vector) -> None:
		
		if self.speed < self.min_speed:
			self.taget_angle= self._TagetAngle(taget_position)
			self.speed 	  	= self.max_speed

		self.speed *= 1-self.attenuation_value
		self._NextPosition(self.taget_angle)

		self.ShowBullet(screen, self.contact_range)
class Normal_Multiple_Bullet(Normal_Bullet, MultipleBullet):
	def __init__(self,
			  	start_position	: Vector,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float,
				taget_position	: Vector,

				shots_angle		: float,
				shots_size		: int,
				shots_cool_time : float,
				shots_spin_speed: float,

		  		shots_contact_range : float,
		  		shots_life_time 	: float,
		  		shots_speed			: float):
		  
		Normal_Bullet.__init__(self, 
						start_position, 
						contact_range, 
						life_time, 
						speed, 
						taget_position)
		
		MultipleBullet.__init__(self, 
						start_position, 
						self.angle, 
						shots_angle, 
						shots_size, 
						shots_cool_time, 
						shots_spin_speed, 

						Normal_Bullet, 
						contact_range = shots_contact_range, 
						life_time 	= shots_life_time, 
						speed 		= shots_speed, 
						taget_position= taget_position)
		
	def Movement(self, 
			  	screen 			: pygame.surface.Surface, 
				taget_position	: Vector) -> None:
		
		Normal_Bullet.Movement(self, screen, None)
		MultipleBullet.Movement(self, screen, taget_position)

class Formation:
	def circle(
			range_ 			: float, 
			size 		  	: int,
			center_position	: Vector,
			bullat_type		: type,
			**bullat_index) -> list:
		
		bullat_angle = 2*math.pi/size
	
		bullets = []
		
		for i in range(size):
			X_Pos = math.cos(bullat_angle*i)*range_ + center_position.x
			Y_Pos = math.sin(bullat_angle*i)*range_ + center_position.y
			
			bullets.append(
				bullat_type(**bullat_index, start_position = Vector(X_Pos, Y_Pos)))
					
		return bullets
		
	def wall(
			range_ 			: float, 
			size 		  	: int,
			location	   	: Vector,
			center_position	: Vector,
			bullat_type		: type,
			**bullat_index) -> list:
				
		bullat_crack = range_/(size-0.999)
		
		bullets = []
				
		for i in range(size):
			if location[1] == 0:
				X_Pos = (range_ * location[0])
				Y_Pos = (bullat_crack*i) - (range_/2)
				
				if 'taget_position' in bullat_index:
					bullat_index['taget_position'] = Vector(-X_Pos + center_position.x, Y_Pos + center_position.y)
			else:
				X_Pos = (bullat_crack*i) - (range_/2)
				Y_Pos = (range_ * location[1])
				
				if 'taget_position' in bullat_index:
					bullat_index['taget_position'] = Vector(X_Pos + center_position.x, -Y_Pos + center_position.y)
			
			bullets.append(
				bullat_type(**bullat_index, start_position = Vector(X_Pos + center_position.x, Y_Pos + center_position.y)))
				
		return bullets
		

if __name__ == "__main__":
	import sys
	import random

	bullets = []

	pygame.init()
	size = [1000, 1000]
	screen = pygame.display.set_mode(size)

	clock = pygame.time.Clock()

	while True:
		MousePos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		StartPos = Vector(random.randint(0,1000), random.randint(0,1000))

		clock.tick(64) 

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:
					bullets += Formation.circle(range_ 		 	= 600,
												size 		   	= 8,
												center_position = MousePos,
												bullat_type 	= Guided_Bullet,
												**bulletsetting['Guided_Bullet'])
					
				if event.key == pygame.K_DOWN:
					bullets += Formation.circle(range_ 		 	= 700,
												size 		   	= 6,
												center_position = MousePos,
												bullat_type 	= Variable_Velocity_Guided_Bullet,
												**bulletsetting['Variable_Velocity_Guided_Bullet'])

				if event.key == pygame.K_RIGHT:
					bullets += Formation.wall(range_ 		 	= 1000,
												size 		   	= 9,
												location		= Vector.Right,
												center_position = MousePos,
												bullat_type 	= Normal_Bullet,
												taget_position  = MousePos,
												**bulletsetting['Normal_Bullet'])
					
				if event.key == pygame.K_LEFT:
					bullets += Formation.wall(range_ 		 	=1000,
												size 		   	= 9,
												location		= Vector.Left,
												center_position = MousePos,
												bullat_type 	= Normal_Multiple_Bullet,
												taget_position  = MousePos,
												**bulletsetting['Normal_Multiple_Bullet'])
				
		screen.fill(Color.white)

		for bullet in bullets:
			bullet.Movement(screen, MousePos)
			if bullet.DelChecker(MousePos): bullets.remove(bullet)

		pygame.display.update()