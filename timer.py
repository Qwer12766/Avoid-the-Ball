import pygame

def start_timer():
    return pygame.time.get_ticks() // 1000  # Get current time in seconds (integer)

def get_elapsed_time(start_time):
    current_time = pygame.time.get_ticks() // 1000
    return current_time - start_time