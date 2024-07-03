import time
import pygame

from dataclasse 		import *
from dataset 			import *
from mainbulletclasse 	import BULLET, MultipleBullet

'''
'' 1. 생성 이펙트, 파괴 이펙트
'' 2. 이동(직진, 추적, 학습)
'' 3. 크기, 속도(속도변화), 최대생존시간
'' 4. 위치, 방향(백터), 생존시간
'''	
class Normal_Bullet(BULLET):
	def __init__(self,
			  	start_position	: Vector2,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float,
				  
				taget_position	: Vector2):
		  
		BULLET.__init__(self, start_position, contact_range, life_time, speed)

		self.angle = self._TagetAngle(taget_position)
		

	def Movement(self,
				screen 			: pygame.surface.Surface, _) -> None:
		
		self._NextPosition(self.angle)
		self.ShowBullet(screen, self.contact_range)
class Guided_Bullet(BULLET):	
	def __init__(self, 
		  		start_position	: Vector2,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float):
		
		BULLET.__init__(self, start_position, contact_range, life_time, speed)


	def Movement(self,
			  	screen			: pygame.surface.Surface,
				taget_position	: Vector2,) -> None:
		
		self._NextPosition(self._TagetAngle(taget_position))
		self.ShowBullet(screen, self.contact_range)
class Variable_Velocity_Guided_Bullet(BULLET):	
	def __init__(self, 
		  		start_position	: Vector2,
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
				taget_position	: Vector2) -> None:
		
		if self.speed < self.min_speed:
			self.taget_angle= self._TagetAngle(taget_position)
			self.speed 	  	= self.max_speed

		self.speed *= 1-self.attenuation_value
		self._NextPosition(self.taget_angle)

		self.ShowBullet(screen, self.contact_range)
class Normal_Multiple_Bullet(Normal_Bullet, MultipleBullet):
	def __init__(self,
			  	start_position	: Vector2,
		  		contact_range 	: float,
		  		life_time 		: float,
		  		speed			: float,
				taget_position	: Vector2,

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
				taget_position	: Vector2) -> None:
		
		Normal_Bullet.Movement(self, screen, None)
		MultipleBullet.Movement(self, screen, taget_position)

if __name__ == "__main__":
	import sys
	import random

	bullets = []

	pygame.init()
	size = [1000, 1000]
	screen = pygame.display.set_mode(size)

	clock = pygame.time.Clock()

	while True:
		MousePos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		StartPos = Vector2(random.randint(0,1000), random.randint(0,1000))

		clock.tick(64) 

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:
					bullets.append(
						Normal_Bullet(
							**bulletsetting['Normal_Bullet'],
							start_position	= StartPos,
							taget_position	= MousePos))
					
				if event.key == pygame.K_DOWN:
					bullets.append(
						Guided_Bullet(
							**bulletsetting['Guided_Bullet'],
							start_position	= StartPos))

				if event.key == pygame.K_RIGHT:
					bullets.append(
						Variable_Velocity_Guided_Bullet( 
							**bulletsetting['Variable_Velocity_Guided_Bullet'],
							start_position	= StartPos))
					
				if event.key == pygame.K_LEFT:
					bullets.append(
						Normal_Multiple_Bullet( 
							**bulletsetting['Normal_Multiple_Bullet'],
							start_position	= StartPos,
							taget_position	= MousePos))
				
		screen.fill(Color['white'])

		for bullet in bullets:
			bullet.Movement(screen, MousePos)
			if bullet.DelChecker(MousePos): bullets.remove(bullet)

		pygame.display.update()