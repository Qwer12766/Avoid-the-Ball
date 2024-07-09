import pygame
from Start_Button import draw_button, draw_best_record
from timer import start_timer, get_elapsed_time
from Moving import draw_character, update_character_position
from save_game_state import load_game_state, save_game_state

# Pygame 초기화 및 화면 설정
pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid_TheBall")

# 한글 폰트 설정 (pygame의 기본 폰트 사용)
pygame.font.init()
font = pygame.font.Font(None, 35)

# 시작 버튼 위치 설정
start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)

# 게임 상태 변수 초기화
character_x, character_y = WIDTH // 2 - 15, HEIGHT // 2 - 15
character_size, character_color, character_speed = 30, (0, 0, 0), 3

timer_running, start_time, best_time = False, None, float('inf')
character_position, timer_running, start_time, best_time = load_game_state()
timer_running = False

# 상태 초기화 함수
def reset_game_state():
    global character_x, character_y, timer_running, start_time
    character_x, character_y = WIDTH // 2 - 15, HEIGHT // 2 - 15
    timer_running, start_time = False, None

# 메인 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not timer_running and start_button_rect.collidepoint(event.pos):
                    timer_running, start_time = True, start_timer()
                    save_game_state((character_x, character_y), timer_running, start_time, best_time)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if timer_running:
                    elapsed_time = get_elapsed_time(start_time)
                    if elapsed_time > best_time:
                        best_time = elapsed_time
                reset_game_state()
                save_game_state((character_x, character_y), timer_running, start_time, best_time)

    screen.fill((255, 255, 255))

    # 시작 버튼 또는 타이머 상태에 따라 그리기
    if not timer_running:
        pygame.mouse.set_visible(True)
        draw_button(screen, 'Start', start_button_rect.x, start_button_rect.y,
                    start_button_rect.width, start_button_rect.height,
                    (100, 100, 100), (150, 150, 150), font)

        # 최고 기록 표시
        if best_time < float('inf'):
            draw_best_record(screen, best_time, font)

    else:
        pygame.mouse.set_visible(False)
        elapsed_time = get_elapsed_time(start_time)
        score_text = f'Your Record: {elapsed_time:.2f}'
        text_surface = font.render(score_text, True, (0, 0, 0))
        screen.blit(text_surface, (20, 20))

        # 캐릭터 위치 업데이트 및 그리기
        character_x, character_y = update_character_position(screen, character_x, character_y, character_size)
        draw_character(screen, character_x, character_y, character_size, character_color)

        # 게임 상태 저장
        save_game_state((character_x, character_y), timer_running, start_time, best_time)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()