import time
import math
import pygame

from dataclasse import *
from dataset 	import *

class BULLET:
	def __init__(self,
			  	start_position	: Vector,
			  	contact_range	: float,
				life_time 		: float,
				speed			: float):
		
		self.contact_range	= contact_range
		self.life_time		= life_time
		self.speed			= speed
		self.position		= start_position
		self.start_life_time= time.time()
		
	def _TagetAngle(self, taget_position : Vector) -> float:

		X_Pos = taget_position.x - self.position.x
		Y_Pos = taget_position.y - self.position.y
		return math.atan2(Y_Pos, X_Pos)
	

	def _NextPosition(self, angle : float) -> None:

		self.position.x += math.cos(angle)*self.speed
		self.position.y += math.sin(angle)*self.speed
		

	def ShowBullet(self, screen, bullet_img) -> None:
		pygame.draw.circle(screen, Color.black, (self.position.x, self.position.y), bullet_img)
		

	def DelChecker(self, taget_position) -> int:

		if self.start_life_time + self.life_time < time.time():
			return 1
		else:
			X_Pos = taget_position.x - self.position.x
			Y_Pos = taget_position.y - self.position.y
			if (X_Pos**2 + Y_Pos**2) < self.contact_range**2:
				return 2
			else:
				return 0

	def Movement(self, screen, taget_position : Vector) -> None:
		self.ShowBullet(screen, self.contact_range)
			

			
class MultipleBullet:
	def __init__(self,
				focus_position	: Vector,
				focus_angle		: float,
				shots_angle		: float,
				shots_size		: int,
				shots_cool_time : float,
				shots_spin_speed: float,
				
				bullat_type		: type,
				**bullat_index):
				
		self.shots = []

		self.start_angle= math.pi + focus_angle - (shots_angle/2)
		self.shot_angle	= shots_angle/(shots_size-1)

		self.shots_size = shots_size

		self.shots_cool_time 		= shots_cool_time
		self.start_shots_cool_time 	= time.time() - shots_cool_time

		self.bullat_type 	= bullat_type
		self.focus_position = focus_position
		self.bullat_index 	= bullat_index
		self.shots_size 	= shots_size

	def Movement(self, 
			  	screen 			: pygame.surface.Surface,
				taget_position	: Vector) -> None:
		
		if self.start_shots_cool_time + self.shots_cool_time < time.time():
			self.start_shots_cool_time = time.time()
			return [
				self.bullat_type(start_position = Vector(self.focus_position.x, self.focus_position.y), 
								taget_position = Vector(math.cos(self.start_angle + (self.shot_angle*i))+ self.focus_position.x, 
														math.sin(self.start_angle + (self.shot_angle*i))+ self.focus_position.y)
,
								**self.bullat_index)
				 for i in range(self.shots_size)]
		return None