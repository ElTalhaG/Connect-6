import pygame
from constants import ROWS, COLS, CELL_SIZE, GRID_COLOR, BOARD_COLOR

class GameBoard:
    def __init__(self, screen):
        self.screen = screen
        self.rows = ROWS
        self.cols = COLS
        self.board = [[0] * self.cols for _ in range(self.rows)]

    def draw(self):
        for r in range(self.rows):
            for c in range(self.cols):
                pygame.draw.rect(self.screen, BOARD_COLOR, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(self.screen, GRID_COLOR, (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
                if self.board[r][c] != 0:
                    pygame.draw.circle(self.screen, self.board[r][c], (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

    def drop_piece(self, col, player):
        for row in reversed(range(self.rows)):
            if self.board[row][col] == 0:
                self.board[row][col] = player.color
                return True
        return False

    def check_winner(self, player):
        color = player.color
        # Check horizontal
        for r in range(self.rows):
            for c in range(self.cols - 5):
                if all(self.board[r][c + i] == color for i in range(6)):
                    return True
        # Check vertical
        for c in range(self.cols):
            for r in range(self.rows - 5):
                if all(self.board[r + i][c] == color for i in range(6)):
                    return True
        # Check diagonal /
        for r in range(5, self.rows):
            for c in range(self.cols - 5):
                if all(self.board[r - i][c + i] == color for i in range(6)):
                    return True
        # Check diagonal \
        for r in range(self.rows - 5):
            for c in range(self.cols - 5):
                if all(self.board[r + i][c + i] == color for i in range(6)):
                    return True
        return False
