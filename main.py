import pygame
import sys
from game_board import GameBoard
from dice import Dice
from player import Player
from constants import WIDTH, HEIGHT, BACKGROUND_COLOR, CELL_SIZE, TERNING_POSITION_X, TERNING_POSITION_Y

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect 6 with Dice')

    game_board = GameBoard(screen)
    dice = Dice()
    player1 = Player('Red', (255, 0, 0))
    player2 = Player('Yellow', (255, 255, 0))
    current_player = player1
    extra_turn = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // CELL_SIZE
                if game_board.drop_piece(col, current_player):
                    if game_board.check_winner(current_player):
                        print(f"{current_player.name} wins!")
                        pygame.quit()
                        sys.exit()
                    
                    if not extra_turn:
                        # Roll the dice
                        roll_result = dice.roll()
                        if roll_result == 'X':
                            print(f"{current_player.name} mister deres tur!")
                            extra_turn = False
                        elif roll_result == '+1':
                            print(f"{current_player.name} får en ekstra tur!")
                            extra_turn = True
                        else:
                            print(f"{current_player.name} kan placere {roll_result} skiver!")
                            extra_turn = False
                    
                    current_player = player2 if current_player == player1 else player1
        
        screen.fill(BACKGROUND_COLOR)
        game_board.draw()
        dice.draw(screen, (TERNING_POSITION_X, TERNING_POSITION_Y))
        pygame.display.flip()

if __name__ == "__main__":
    main()
