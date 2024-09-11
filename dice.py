import random
import pygame
from constants import TERNING_FARVE, TERNING_KANT_FARVE, TEXT_FARVE, TERNING_STØRRELSE

class Dice:
    def __init__(self):
        self.current_value = 1
    
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

    def draw(self, screen, position):
        # Tegn terning (en firkant)
        pygame.draw.rect(screen, TERNING_FARVE, (position[0], position[1], TERNING_STØRRELSE, TERNING_STØRRELSE))
        pygame.draw.rect(screen, TERNING_KANT_FARVE, (position[0], position[1], TERNING_STØRRELSE, TERNING_STØRRELSE), 5)

        # Vis terningens resultat som tekst
        font = pygame.font.SysFont(None, 55)
        if isinstance(self.current_value, int):
            text = font.render(str(self.current_value), True, TEXT_FARVE)
        else:
            text = font.render(self.current_value, True, TEXT_FARVE)
        
        text_rect = text.get_rect(center=(position[0] + TERNING_STØRRELSE // 2, position[1] + TERNING_STØRRELSE // 2))
        screen.blit(text, text_rect)
