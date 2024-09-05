import pygame
import sys
from game_board import GameBoard
from dice import Dice
from player import Player
from constants import WIDTH, HEIGHT, BACKGROUND_COLOR, CELL_SIZE

def main():
    pygame.init()
    skærm = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect 6 med Terning')
    
    spillebræt = GameBoard(skærm)
    terning = Dice()
    spiller1 = Player('Rød', (255, 0, 0))
    spiller2 = Player('Gul', (255, 255, 0))
    nuværende_spiller = spiller1
    ekstra_tur = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                kolonne = event.pos[0] // CELL_SIZE
                if spillebræt.drop_piece(kolonne, nuværende_spiller):
                    if spillebræt.check_winner(nuværende_spiller):
                        print(f"{nuværende_spiller.name} vinder!")
                        pygame.quit()
                        sys.exit()
                    if not ekstra_tur:
                        # Kast terningen
                        ternings_resultat = terning.roll()
                        if ternings_resultat == 'X':
                            print(f"{nuværende_spiller.name} mister deres tur!")
                            ekstra_tur = False
                        elif ternings_resultat == '+1':
                            print(f"{nuværende_spiller.name} får en ekstra tur!")
                            ekstra_tur = True
                        else:
                            print(f"{nuværende_spiller.name} kan placere {ternings_resultat} brikker!")
                            ekstra_tur = False
                    nuværende_spiller = spiller2 if nuværende_spiller == spiller1 else spiller1
                    
        skærm.fill(BACKGROUND_COLOR)
        spillebræt.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()
