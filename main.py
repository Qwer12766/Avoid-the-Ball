import pygame
import sys
from button import draw_button
from timer import start_timer, get_elapsed_time
from character import Character

# Pygame 초기화
pygame.init()

# 화면 설정
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball game")

# 한글 폰트 설정 (시스템 폰트 사용)
pygame.font.init()
available_fonts = pygame.font.get_fonts()

# 여러 폰트 이름을 시도하여 한글을 지원하는 폰트를 찾기
preferred_fonts = ["malgungothic", "nanummyeongjo", "d2coding", "gulim"]

for font_name in preferred_fonts:
    if font_name in available_fonts:
        font = pygame.font.SysFont(font_name, 35)
        break
else:
    print("적절한 한글 폰트를 찾을 수 없습니다.")
    sys.exit()

# 타이머와 게임 상태 변수 초기화
start_time = None
timer_running = False

# 캐릭터 초기화
character = Character(screen, width // 2, height // 2)

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
    
    # 키 입력 처리 (캐릭터 움직임)
    keys = pygame.key.get_pressed()
    if timer_running:
        character.move(keys)
    
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
        
        # 캐릭터 그리기
        character.draw()
    
    pygame.display.flip()
    pygame.time.delay(10)  # CPU 과부하 줄이기
    pygame.display.update()

# Pygame 종료 및 프로그램 종료
pygame.quit()
sys.exit()