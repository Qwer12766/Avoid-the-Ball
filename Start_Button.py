import pygame

def draw_button(screen, text, x, y, width, height, inactive_color, active_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_rect = pygame.Rect(x, y, width, height)

    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, active_color, button_rect)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, inactive_color, button_rect)

    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return False