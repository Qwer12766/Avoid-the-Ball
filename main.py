import pygame #모듈

pygame.init() #파이 게임 초기화
display_width = 700
display_height = 700
screen = pygame.display.set_mode((700, 700)) #화면 크기
clock = pygame.time.Clock() 
pygame.display.set_caption("Ball game") #이름
gameDisplay = pygame.display.set_mode((display_width, display_height))



while True: #게임 루프
    screen.fill((255, 255, 255))

    #변수 업데이트

    event = pygame.event.poll()
    if event.type == pygame.QUIT:

        break


    #화면 그리기


    pygame.display.update() #모든 화면 그리기 업데이트

    clock.tick(60)

import button
import text_objects
largeText = pygame.font.SysFont("malgungothic",115)
TextSurf, TextRect = text_objects("Ball game", largeText)
TextRect.center = ((display_width/2),(display_height/2))
gameDisplay.blit(TextSurf, TextRect)


pygame.quit()    