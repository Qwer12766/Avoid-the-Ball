import time
import math
import pygame

from bullet.dataclasse	import *
from bullet.dataset 	import *

class BULLET:
	def __init__(self,
			  	start_position	: Vector,
			  	contact_range	: float,
				life_time 		: float,
				speed			: float):
		
		self.contact_range	= contact_range
		self.life_time		= life_time
		self.speed			= speed
		self.position		= Vector(start_position.x, start_position.y)
		self.position_before= Vector(start_position.x, start_position.y)
		self.start_life_time= time.time()
		
	def _targetAngle(self, target_position : Vector) -> float:

		X_Pos = target_position.x - self.position.x
		Y_Pos = target_position.y - self.position.y
		return math.atan2(Y_Pos, X_Pos)
	

	def _NextPosition(self, angle : float) -> None:
		self.position_before = Vector(self.position.x, self.position.y)
		self.position.x += math.cos(angle)*self.speed
		self.position.y += math.sin(angle)*self.speed
		

	def ShowBullet(self, screen, shadow_color, bullet_img) -> None:
		pygame.draw.circle(screen, shadow_color, (self.position_before.x, self.position_before.y), bullet_img)
		pygame.draw.circle(screen, Color.black, (self.position.x, self.position.y), bullet_img)
		

	def DelChecker(self, target_position) -> int:

		if self.start_life_time + self.life_time < time.time():
			return 1
		else:
			X_Pos = target_position.x - self.position.x
			Y_Pos = target_position.y - self.position.y
			if (X_Pos**2 + Y_Pos**2) < self.contact_range**2:
				return 2
			else:
				return 0

	def Movement(self, screen, target_position : Vector) -> None:
		self.ShowBullet(screen, Color.black, self.contact_range)
			

			
class MultipleBullet:
	def __init__(self,
			  	focus_position	: Vector,
				focus_angle		: float,
				shots_angle		: float,
				shots_size		: int,
				shots_cool_time : float,
				shots_spin_angle: float,

				bullat_type		: type,
				**bullat_index):

		self.shots = []
		
		self.start_angle= math.pi + focus_angle - (shots_angle/2)
		self.shot_angle	= shots_angle/(shots_size-0.9999)

		self.shots_size = shots_size

		self.shots_cool_time 		= shots_cool_time
		self.start_shots_cool_time 	= time.time() - shots_cool_time

		self.bullat_type 	= bullat_type
		self.focus_position = focus_position
		self.bullat_index 	= bullat_index
		self.shots_size 	= shots_size
		self.shots_spin_angle=shots_spin_angle

	def Movement(self, start_position	: Vector) -> None:
		
		if self.start_shots_cool_time + self.shots_cool_time < time.time():
			self.start_shots_cool_time = time.time()
			self.start_angle += self.shots_spin_angle
			
			return [
				self.bullat_type(start_position = Vector(start_position.x, start_position.y), 
								target_position = Vector(math.cos(self.start_angle + (self.shot_angle*i))+ start_position.x, 
														math.sin(self.start_angle + (self.shot_angle*i))+ start_position.y),
								**self.bullat_index)
								for i in range(self.shots_size)]
		
		return None