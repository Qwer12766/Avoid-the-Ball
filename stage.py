import copy

from bullet import *
from bullet.dataset import stagesettion

class Stage:
	Number = 0
	stages = []

	def Checke(self, time, target_position):
		bullets = []

		if stagesettion[self.Number][0] <= time:
			self.stages.append([time - stagesettion[self.Number][1], stagesettion[self.Number][1], stagesettion[self.Number][2]])
			self.Number += 1

		for stage_ in self.stages:
			if stage_[0] + stage_[1] < time:
				stage_[0] = time

				for stage_index in stage_[2]:
					stage_index_ = copy.deepcopy(stage_index)
					if stage_index_['other']['target_position'] == 'target_position': stage_index_['other']['target_position'] = target_position
					
					if 	 stage_index_['formation'] == 'circle': bullets += Formation.circle(bullat_type = globals()[stage_index_['bullat_type']], **stage_index_['other'])
					elif stage_index_['formation'] == 'wall': 	bullets += Formation.wall(	bullat_type = globals()[stage_index_['bullat_type']], **stage_index_['other'])
					else:
						bullets.append(globals()[stage_index_['bullat_type']](**stage_index_['other']))
		return bullets

if __name__ == "__main__":
	import sys
	import pygame
	import time
	
	Stage = Stage()
	bullets = []
	pygame.init()
	size = [700, 700]
	screen = pygame.display.set_mode(size)
	t_surface = screen.convert_alpha()

	clock = pygame.time.Clock()
	time_ = time.time()
	screen.fill((255, 255, 255))
	GAME = True	
	while GAME:
		clock.tick(64)
		MousePos = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

		bullets += Stage.Checke(time.time() - time_, MousePos)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		t_surface.fill((255, 255, 255, 80))
		screen.blit(t_surface, (0, 0))

		for bullet in bullets:
			shots = bullet.Movement(screen, MousePos)
			if shots: bullets += shots

			Del_Checke = bullet.DelChecker(MousePos)

			if Del_Checke == 1: bullets.remove(bullet)
			elif Del_Checke == 2:
				#GAME = False
				print('GameOver')

		pygame.display.flip()