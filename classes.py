from consts import *
import pygame as pg


def check_coords(y, x):
    if 0 <= x <= (SCREEN[0] // CELL_WIDTH) - 1 and 0 <= y <= (SCREEN[1] // CELL_WIDTH) - 1:
        return True
    else:
        return False


def check_neighbours(matrix, i, j):
    alive = 0
    if check_coords(i - 1, j) and matrix[i - 1][j][2] is True:
        alive += 1
    if check_coords(i + 1, j) and matrix[i + 1][j][2] is True:
        alive += 1
    if check_coords(i - 1, j - 1) and matrix[i - 1][j - 1][2] is True:
        alive += 1
    if check_coords(i - 1, j + 1) and matrix[i - 1][j + 1][2] is True:
        alive += 1
    if check_coords(i + 1, j - 1) and matrix[i + 1][j - 1][2] is True:
        alive += 1
    if check_coords(i + 1, j + 1) and matrix[i + 1][j + 1][2] is True:
        alive += 1
    if check_coords(i, j + 1) and matrix[i][j + 1][2] is True:
        alive += 1
    if check_coords(i, j - 1) and matrix[i][j - 1][2] is True:
        alive += 1
    return alive


class Config:
    def __init__(self, matrix):
        self.matrix = matrix

    def update(self):
        temp = [[[j, i, False] for j in range(0, SCREEN[0], CELL_WIDTH)] for i in range(0, SCREEN[1], CELL_WIDTH)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                alive = check_neighbours(self.matrix, i, j)
                if self.matrix[i][j][2] is True:
                    if alive < 2 or alive > 3:
                        temp[i][j][2] = False
                    else:
                        temp[i][j][2] = True
                else:
                    if alive == 3:
                        temp[i][j][2] = True
                    else:
                        temp[i][j][2] = False
        self.matrix = temp

    def draw(self, surface):
        for i in self.matrix:
            for j in i:
                if j[2] is True:
                    pg.draw.rect(surface, WHITE, pg.Rect(j[0], j[1], CELL_WIDTH, CELL_WIDTH))
                else:
                    pg.draw.rect(surface, WHITE, pg.Rect(j[0], j[1], CELL_WIDTH, CELL_WIDTH), 1)

