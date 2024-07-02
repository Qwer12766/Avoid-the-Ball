import pygame
import sys
import json
from button import draw_button
from timer import start_timer, get_elapsed_time
from character import Character
from save_game_state import save_game_state, load_game_state

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

# 시작 버튼 위치 (화면 중앙)
start_button_rect = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 100)

# 게임 상태 변수 초기화
character = None
timer_running = False
start_time = None
best_time = float('inf')

# 최고 기록 초기화 및 저장된 게임 상태 불러오기
character_position, timer_running, start_time, best_time = load_game_state()

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
            if not timer_running and start_button_rect.collidepoint(event.pos):
                character = Character(screen, width // 2 - 15, height // 2 - 15, 30, (0, 0, 0), 2)  # 중앙에 위치하도록 수정
                timer_running = True
                start_time = start_timer()  # 타이머 시작
                print("게임 시작")  # 게임 시작 메시지 출력
                # 게임 상태 저장
                save_game_state((character.x, character.y), timer_running, start_time, best_time)

    # 화면 업데이트
    screen.fill((255, 255, 255))

    if not timer_running:
        # 시작 버튼 그리기
        draw_button(screen, '시작', start_button_rect.x, start_button_rect.y, start_button_rect.width, start_button_rect.height,
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

        # 캐릭터가 초기화되었을 때만 그리기
        if character:
            keys = pygame.key.get_pressed()
            character.update_position(keys, width, height)  # 화면의 너비와 높이 전달
            character.draw()

            # 게임 상태 저장 (캐릭터 움직임이 발생할 때마다 저장)
            save_game_state((character.x, character.y), timer_running, start_time, best_time)

    pygame.display.flip()
    pygame.time.delay(10)  # CPU 과부하 줄이기

# Pygame 종료 및 프로그램 종료
pygame.quit()
sys.exit()