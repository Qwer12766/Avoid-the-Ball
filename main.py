import pygame
import sys
from button import draw_button
from timer import start_timer, get_elapsed_time

# Pygame 초기화
pygame.init()

# 화면 설정
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball game")

# 한글이 안나와!!!!
pygame.font.init()  # 한글이 안나와!!!!
font = pygame.font.Font(None, 35)

# 타이머와 게임 상태 변수 초기화
start_time = None
timer_running = False

# 메인 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 시작 버튼이 클릭되었는지 확인
            if not timer_running:
                mouse_pos = pygame.mouse.get_pos()
                start_button_rect = pygame.Rect(width/2 - 100, height/2 - 50, 200, 100)
                if start_button_rect.collidepoint(mouse_pos):
                    timer_running = True
                    start_time = start_timer()  # 타이머 시작
                    print("게임 시작")  # 게임 시작 메시지 출력
    
    # 화면 업데이트
    screen.fill((255, 255, 255))
    
    if not timer_running:
        # 게임이 시작되지 않았을 때 시작 버튼 그리기
        draw_button(screen, '시작', width/2 - 100, height/2 - 50, 200, 100,
                    (100, 100, 100), (150, 150, 150), font)
    else:
        # 게임이 시작된 경우
        
        # 경과된 시간 계산
        elapsed_time = get_elapsed_time(start_time)
        
        # 타이머 표시 (점수 대신)
        score_text = f'시간: {elapsed_time}'
        score_surface = font.render(score_text, True, (0, 0, 0))
        score_rect = score_surface.get_rect(topleft=(20, 20))
        screen.blit(score_surface, score_rect)
    
    pygame.display.flip()
    pygame.time.delay(10)  # CPU 과부하줄이기
    pygame.display.update()

# Pygame 종료 및 프로그램 종료
pygame.quit()
sys.exit()