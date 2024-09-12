import pygame
import random
from constants import DICE_SIZE

class Dice:
    def __init__(self):
        self.current_value = None

    def roll(self):
        roll = random.randint(1, 10)
        if roll in [1, 2, 3]:
            self.current_value = 1
        elif roll in [4, 5, 6]:
            self.current_value = 2
        elif roll in [7, 8]:
            self.current_value = 3
        elif roll == 9:
            self.current_value = 'X'
        elif roll == 10:
            self.current_value = '+1'
        return self.current_value

    def draw(self, screen, x, y, size, color):
        pygame.draw.rect(screen, color, (x, y, size, size))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, size, size), 3)
        font = pygame.font.SysFont(None, 36)
        text = font.render(str(self.current_value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(x + size // 2, y + size // 2))
        screen.blit(text, text_rect)
