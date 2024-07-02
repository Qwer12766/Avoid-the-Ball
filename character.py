import pygame

class Character:
    def __init__(self, screen, x, y, size, color, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 3

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

    def update_position(self, keys, screen_width, screen_height):
        if keys[pygame.K_w] and self.y > 0:  # 위쪽 방향키
            self.y -= self.speed
        if keys[pygame.K_s] and self.y < screen_height - self.size:  # 아래쪽 방향키
            self.y += self.speed
        if keys[pygame.K_a] and self.x > 0:  # 왼쪽 방향키
            self.x -= self.speed
        if keys[pygame.K_d] and self.x < screen_width - self.size:  # 오른쪽 방향키
            self.x += self.speed