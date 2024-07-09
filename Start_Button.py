import pygame

def draw_button(screen, text, x, y, width, height, inactive_color, active_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, width, height)

    # 색상 설정 및 버튼 그리기
    color = active_color if button_rect.collidepoint(mouse) else inactive_color
    pygame.draw.rect(screen, color, button_rect)

    # 텍스트 렌더링
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

def draw_best_record(screen, best_time, font):
    best_time_text = f'Best Record: {best_time:.2f}'
    best_time_surface = font.render(best_time_text, True, (0, 0, 0))
    screen.blit(best_time_surface, (20, 20))