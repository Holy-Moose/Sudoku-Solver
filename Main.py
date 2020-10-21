# Sudoku solver using Pgame and backtracking


import pygame
from sudokusolver import Solve, valid

pygame.init()
clock = pygame.time.Clock()

screenWidth = 453
screenHeight = 453
screenName = 'Sudoku Solver'

WHITE = (255,255,255,255)
BLACK = (0,0,0,0)
RED = (255,0,0,255)

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(screenName)

class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]
                    ]
        self.active = None
        self.activeX = None
        self.activeY = None

    def DrawGrid(self):
        for i in range (0,10):
            x = (i * self.width)
            if i % 3 == 0:
                pygame.draw.line(win, WHITE, (x, 0), (x, screenHeight), 4)
            else:
                pygame.draw.line(win, WHITE, (x, 0), (x, screenHeight), 1)

        for i in range (0,10):
            y = (i * self.height)
            if i % 3 == 0:
                pygame.draw.line(win, WHITE, (0, y), (screenWidth, y), 4)
            else:
                pygame.draw.line(win, WHITE, (0, y), (screenWidth, y), 1)

        if self.active:
            pygame.draw.rect(win, WHITE, (self.activeX, self.activeY, self.width, self.height))

    def DrawNumbers(self):
        for r in range(len(self.grid)):
            # r = row
            for c in range(len(self.grid[r])):
                #c = column
                if self.grid[r][c] != 0:
                    font = pygame.font.SysFont('Arial', 30, True, False)
                    if self.active and self.active == (r,c):
                        text = font.render(str(self.grid[r][c]), 1, BLACK)
                    else:
                        text = font.render(str(self.grid[r][c]), 1, WHITE)

                    x = (c * self.width) + ((self.width - text.get_width()) // 2)
                    y = (r * self.height) + ((self.height - text.get_height()) // 2)
                    win.blit(text, (x, y))


    def ActiveGrid(self, row, col):
        if self.active and self.active == (row, col):
            self.active = None
        elif row >= 0 and row <=8 and col >= 0 and col <= 8:
            self.active = (row, col)
            self.activeX = col * self.width
            self.activeY = row * self.height

    def UpdateGrid(self, num):
        if grid.active:
            if valid(self.grid, num, self.active) or num == 0:
                self.grid[self.active[0]][self.active[1]] = num

    def ClearGrid(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = 0


def redrawGameWindow():
    win.fill(BLACK)
    grid.DrawGrid()
    grid.DrawNumbers()

    pygame.display.update()

def mainLoop():
    run = True
    global grid
    grid = Grid(50, 50)
    while run:
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                grid.ActiveGrid((pos[1] // 50), (pos[0] // 50))

        keys = pygame.key.get_pressed()
        if grid.active and keys[pygame.K_LEFT]:
            grid.ActiveGrid(grid.active[0], (grid.active[1] - 1))
        if grid.active and keys[pygame.K_UP]:
            grid.ActiveGrid((grid.active[0] - 1), grid.active[1])
        if grid.active and keys[pygame.K_RIGHT]:
            grid.ActiveGrid(grid.active[0], (grid.active[1] + 1))
        if grid.active and keys[pygame.K_DOWN]:
            grid.ActiveGrid((grid.active[0] + 1), grid.active[1])

        if keys[pygame.K_1]:
            grid.UpdateGrid(1)
        if keys[pygame.K_2]:
            grid.UpdateGrid(2)
        if keys[pygame.K_3]:
            grid.UpdateGrid(3)
        if keys[pygame.K_4]:
            grid.UpdateGrid(4)
        if keys[pygame.K_5]:
            grid.UpdateGrid(5)
        if keys[pygame.K_6]:
            grid.UpdateGrid(6)
        if keys[pygame.K_7]:
            grid.UpdateGrid(7)
        if keys[pygame.K_8]:
            grid.UpdateGrid(8)
        if keys[pygame.K_9]:
            grid.UpdateGrid(9)
        if keys[pygame.K_DELETE] or keys[pygame.K_BACKSPACE]:
            grid.UpdateGrid(0)
        if keys[pygame.K_RETURN]:
            Solve(grid.grid)
        if keys[pygame.K_c]:
            grid.ClearGrid()

        redrawGameWindow()

mainLoop()
pygame.quit()
