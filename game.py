import pygame

WINDOW_WIDTH = 450
WIDOW_HEIGHT = 450
BG_COLOR = (255, 255, 255)
LENGTH = 150

pygame.init()
screenA = pygame.display.set_mode([WINDOW_WIDTH, WIDOW_HEIGHT])
screenA.fill(BG_COLOR)


class GuiBuilder:
    def __init__(self, row, col, square, screen, width, length, height):
        self.row = row
        self.col = col
        self.square = square
        self.screen = screen
        self.width = width
        self.length = length
        self.height = height

    def board_builder(self, k, w_gap, h_gap, m_fixer, divider, length):
        for i in range(1, self.row):
            for j in range(1, self.col):
                pygame.draw.line(self.screen, (0, 0, 0), (w_gap, j * self.length / divider + h_gap),
                                 (self.width, j * self.length / divider + h_gap), width=1)
                for y in range(k, self.square):
                    pygame.draw.line(self.screen, (0, 0, 0), (w_gap, y * length),
                                     (self.width, y * length), width=3)
            pygame.draw.line(self.screen, (0, 0, 0), (w_gap + i * self.length / divider, h_gap),
                             (w_gap + i * self.length / divider, self.height), width=1)
            for y in range(k, self.square):
                pygame.draw.line(self.screen, (0, 0, 0), (y * length+m_fixer, h_gap),
                                 (y * length+m_fixer, self.height), width=3)
            pygame.display.update()

    def print_to_board(self, col, row, value, width):
        myFont = pygame.font.SysFont(None, 30, italic=True)
        pygame.font.init()
        sq_gap = width / self.row
        x = col * sq_gap
        y = row * sq_gap
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, sq_gap, sq_gap), 0)
        # print(value)
        text = myFont.render(str(value), True, (0, 0, 0))

        self.screen.blit(text, (x + (sq_gap / 2 - text.get_width() / 2),
                                y + (sq_gap / 2 - text.get_height() / 2)))
        pygame.draw.rect(self.screen, (2, 147, 251), (x, y, sq_gap, sq_gap), 3)
        pygame.display.update()

    def print_initialised_board(self, board, width, w_gap, h_gap, text_size):
        myFont = pygame.font.SysFont(None, text_size, italic=True)
        pygame.font.init()
        for i in range(self.row):
            for j in range(self.col):
                if board[j][i] != 0:
                    text = myFont.render(str(board[j][i]), True, (0, 0, 0))
                    self.screen.blit(text, (i * (width / self.row) + (width / self.row // self.square)+w_gap,
                                            j * (width / self.col) + (width / self.col // self.square)+h_gap))
                    pygame.display.update()

    def userMessage(self):
        myFont = pygame.font.SysFont(None, 15, italic=True)
        text = myFont.render("Choose a Sudoku to S O L V E", True, (0, 180, 0))
        self.screen.blit(text, (150, 220))


class GameLogic:
    def __init__(self, game_board):
        self.game_board = game_board
        self.screen = pygame.display.set_mode([WINDOW_WIDTH, WIDOW_HEIGHT])
        self.screen.fill((255, 255, 255))
        self.gui = GuiBuilder(9, 9, 3, self.screen, WINDOW_WIDTH, LENGTH, WIDOW_HEIGHT)
        self.gui.board_builder(1, 0, 0, 0, 3, 150)
        self.gui.print_initialised_board(self.game_board, 450, 0, 0, 30)

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
                self.gui.print_to_board(col, row, self.game_board[row][col], 450)
                pygame.display.update()
                pygame.time.delay(10)
                if self.solve_sudoku(game_board):
                    return True
                self.game_board[row][col] = 0
                self.gui.print_to_board(col, row, self.game_board[row][col], 450)
                pygame.display.update()
                pygame.time.delay(10)

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
    boardB = [
        [5, 0, 9, 0, 0, 0, 4, 0, 0],
        [7, 0, 8, 3, 0, 4, 9, 0, 0],
        [6, 0, 1, 0, 0, 0, 7, 3, 0],
        [4, 6, 2, 5, 0, 0, 0, 0, 0],
        [3, 8, 5, 7, 2, 0, 6, 4, 9],
        [1, 0, 7, 4, 0, 8, 2, 0, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 4],
        [0, 0, 3, 0, 4, 0, 0, 8, 7],
        [0, 7, 0, 0, 5, 3, 0, 0, 6]
    ]
    rectOne = pygame.Rect(70, 50, 150, 150)
    rectTwo = pygame.Rect(230, 50, 150, 150)
    loopRunner = True
    pygame.draw.rect(screenA, (0, 0, 0), rectOne, width=2)
    gui = GuiBuilder(9, 9, 4, screenA, 220, 150, 200)
    gui.board_builder(2, 70, 50, 20, 9, 50)
    gui.print_initialised_board(board, 150, 70, 50, 15)

    pygame.draw.rect(screenA, (0, 0, 0), rectTwo, width=2)
    gui2 = GuiBuilder(9, 9, 4, screenA, 380, 150, 200)
    gui2.board_builder(2, 230, 50, 180, 9, 50)
    gui2.print_initialised_board(boardB, 150, 230, 50, 15)

    gui.userMessage()

    hover = True
    while loopRunner:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loopRunner = False
            if pygame.Rect.collidepoint(rectOne, pygame.mouse.get_pos()):
                pygame.draw.rect(screenA, (255, 0, 0), rectOne, width=2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hover = False
                    if not hover and pygame.Rect(70, 50, 150, 150).collidepoint(event.pos):
                        screenA.fill(BG_COLOR)
                        game = GameLogic(board)
                        game.solve_sudoku(board)
            else:
                pygame.draw.rect(screenA, (0, 0, 0), rectOne, width=2)

            if pygame.Rect.collidepoint(rectTwo, pygame.mouse.get_pos()):
                pygame.draw.rect(screenA, (255, 0, 0), rectTwo, width=2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("need to clear screen")
                    screenA.fill(BG_COLOR)
                    pygame.display.update()
                    game = GameLogic(boardB)
                    game.solve_sudoku(boardB)
            else:
                pygame.draw.rect(screenA, (0, 0, 0), rectTwo, width=2)
        pygame.display.update()


if __name__ == "__main__":
    main()
