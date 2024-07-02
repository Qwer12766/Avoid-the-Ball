import pygame

class Character:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 3  # 캐릭터의 이동 속도
        self.width = 35  # 캐릭터의 너비
        self.height = 35  # 캐릭터의 높이
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()  # 화면 크기 가져오기

    def draw(self):
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.x, self.y, self.width, self.height))  # 사각형
    def move(self, keys):
        if keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.speed
        if keys[pygame.K_s]:
            if self.y < self.screen_height - self.height:
                self.y += self.speed
        if keys[pygame.K_a]:
            if self.x > 0:
                self.x -= self.speed
        if keys[pygame.K_d]:
            if self.x < self.screen_width - self.width:
                self.x += self.speed