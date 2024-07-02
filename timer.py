import pygame

def start_timer():
    return pygame.time.get_ticks() // 1000  # 현재 시간을 초 단위로 반환

def get_elapsed_time(start_time):
    current_time = pygame.time.get_ticks() // 1000
    elapsed_time = current_time - start_time
    return elapsed_time