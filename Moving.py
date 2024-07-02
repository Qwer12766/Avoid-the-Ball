import pygame

def draw_character(screen, x, y, size, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))

def update_character_position(keys, screen_width, screen_height, x, y, size, speed):
    # 키 입력에 따라 캐릭터 위치 업데이트
    new_x = x - (keys[pygame.K_a] and x > 0) * speed
    new_x = new_x + (keys[pygame.K_d] and new_x < screen_width - size) * speed
    new_y = y - (keys[pygame.K_w] and y > 0) * speed
    new_y = new_y + (keys[pygame.K_s] and new_y < screen_height - size) * speed
    
    return new_x, new_y