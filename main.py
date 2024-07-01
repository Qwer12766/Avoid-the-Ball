import pygame #모듈

pygame.init() #파이 게임 초기화
screen = pygame.display.set_mode((700, 700)) #화면 크기
clock = pygame.time.Clock() 
pygame.display.set_caption("Ball game") #이름



while True: #게임 루프
    screen.fill((255, 255, 255))

    #변수 업데이트

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    #화면 그리기

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(60)

pygame.quit()    