import pygame
import sys
from game_board import GameBoard
from dice import Dice
from player import Player
from constants import WIDTH, HEIGHT, BOARD_WIDTH, BACKGROUND_COLOR, CELL_SIZE, TEXT_COLOR, DICE_SIZE

def display_ui(screen, player1, player2, current_player, dice):
    # Display player information
    font = pygame.font.SysFont(None, 36)
    player1_score_text = font.render(f'{player1.name} Skiver: {player1.pieces}', True, TEXT_COLOR)
    player2_score_text = font.render(f'{player2.name} Skiver: {player2.pieces}', True, TEXT_COLOR)
    turn_text = font.render(f'Tur: {current_player.name}', True, current_player.color)

    # Place UI elements outside the board
    screen.blit(player1_score_text, (BOARD_WIDTH + 50, 50))  # Right side of the board
    screen.blit(player2_score_text, (BOARD_WIDTH + 50, 100))  # Right side of the board
    screen.blit(turn_text, (BOARD_WIDTH + 50, 150))  # Right side of the board

    # Display dice information
    dice.draw(screen, BOARD_WIDTH + 50, 200, DICE_SIZE, current_player.color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Adjust window size
    pygame.display.set_caption('Connect 6 with Dice')

    # Initialize game components
    game_board = GameBoard(screen)
    dice = Dice()
    player1 = Player('Red', (255, 0, 0))
    player2 = Player('Yellow', (255, 255, 0))
    current_player = player1
    extra_turn = False
    pieces_to_place = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // CELL_SIZE
                if col < game_board.cols:  # Ensure clicks are within the board
                    if pieces_to_place > 0:  # Only allow placement if player has pieces to place
                        if game_board.drop_piece(col, current_player):
                            pieces_to_place -= 1
                            current_player.pieces += 1
                            if game_board.check_winner(current_player):
                                print(f"{current_player.name} wins!")
                                pygame.quit()
                                sys.exit()
                        if pieces_to_place == 0:  # Once pieces are placed, switch player
                            current_player = player2 if current_player == player1 else player1
                            extra_turn = False

                    if pieces_to_place == 0 and not extra_turn:  # Only roll if no pieces left to place
                        roll_result = dice.roll()
                        if roll_result == 'X':
                            print(f"{current_player.name} loses their turn!")
                            current_player = player2 if current_player == player1 else player1
                        elif roll_result == '+1':
                            print(f"{current_player.name} gets an extra turn! Adding 1 to the next roll.")
                            extra_turn = True
                        else:
                            pieces_to_place = roll_result
                            print(f"{current_player.name} can place {pieces_to_place} pieces!")

                    if extra_turn and pieces_to_place == 0:  # Handle extra turn with +1 logic
                        roll_result = dice.roll()
                        if isinstance(roll_result, int):
                            pieces_to_place = roll_result + 1  # Add 1 to next roll
                            print(f"Extra turn! {current_player.name} places {pieces_to_place} pieces.")
                            extra_turn = False

        screen.fill(BACKGROUND_COLOR)
        game_board.draw()
        display_ui(screen, player1, player2, current_player, dice)  # Display text and dice
        pygame.display.flip()

if __name__ == "__main__":
    main()
