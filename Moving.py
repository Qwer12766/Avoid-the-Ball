import pygame

def draw_character(screen, x, y, size, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))

def update_character_position(screen, x, y, size):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x - size // 2, mouse_y - size // 2