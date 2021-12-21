import pygame

WINDOW_WIDTH = 450
WIDOW_HEIGHT = 450
BG_COLOR = (255, 255, 255)
LENGTH = 150


class GameLogic:
    def __init__(self, game_board):
        self.game_board = game_board

    def check_empty_location(self):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board)):
                if self.game_board[i][j] == 0:
                    location = [i, j]
                    return location
        # return False

    # check if num is already in that row or not
    def check_num_inRow(self, col, num):
        for x in range(len(self.game_board)):
            if self.game_board[x][col] == num:
                return True
        return False

    # check if num is already in that col or not
    def check_num_inCol(self, row, num):
        for y in range(len(self.game_board)):
            if self.game_board[row][y] == num:
                return True
        return False

    # check if num is already in the grid or not
    def check_num_inGrid(self, row, col, num):
        grid = 3
        for i in range(row // grid * grid, row // grid * grid + grid):
            for j in range(col // grid * grid, col // grid * grid + grid):
                if self.game_board[i][j] == num:
                    return True
        return False

    def check_location_isSafe(self, location, num):
        row = location[0]
        col = location[1]
        if not self.check_num_inRow(col, num) and not self.check_num_inCol(row, num) and \
                not self.check_num_inGrid(row, col, num):
            return True

    def solve_sudoku(self, game_board):
        location = self.check_empty_location()
        if not location:
            return True

        row = location[0]
        col = location[1]

        for num in range(1, 10):
            if self.check_location_isSafe(location, num):
                # if num is safe then assign it to the location and recursively call the function
                # else change the location value back to 0
                self.game_board[row][col] = num
                if self.solve_sudoku(game_board):
                    return True
                self.game_board[row][col] = 0

        return False


def main():
    board = [
        [0, 7, 2, 0, 0, 4, 9, 0, 0],
        [3, 0, 4, 0, 8, 9, 1, 0, 0],
        [8, 1, 9, 0, 0, 6, 2, 5, 4],
        [7, 0, 1, 0, 0, 0, 0, 9, 5],
        [9, 0, 0, 0, 0, 2, 0, 7, 0],
        [0, 0, 0, 8, 0, 7, 0, 1, 2],
        [4, 0, 5, 0, 0, 1, 6, 2, 0],
        [2, 3, 7, 0, 0, 0, 5, 0, 1],
        [0, 0, 0, 0, 2, 5, 7, 0, 0]
    ]
    loopRunner = True
    game = GameLogic(board)
    game.solve_sudoku(board)

    for i in range(len(board)):
        print(board[i])


if __name__ == "__main__":
    main()
