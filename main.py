from classes import *
import pygame as pg

screen = pg.display.set_mode(SCREEN)
pg.display.set_caption(CAPTION)
playing = True
starting = False
config = Config([[[j, i, False] for j in range(0, SCREEN[0], CELL_WIDTH)] for i in range(0, SCREEN[1], CELL_WIDTH)])

while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.MOUSEBUTTONDOWN and not starting:
            x, y = pg.mouse.get_pos()
            x -= x % CELL_WIDTH
            y -= y % CELL_WIDTH
            if config.matrix[y // CELL_WIDTH][x // CELL_WIDTH][2] is False:
                config.matrix[y // CELL_WIDTH][x // CELL_WIDTH] = [x, y, True]
            else:
                config.matrix[y // CELL_WIDTH][x // CELL_WIDTH] = [x, y, False]
        elif event.type == pg.KEYDOWN and not starting:
            if event.key == pg.K_SPACE:
                starting = True
    screen.fill(BLACK)
    if starting is True:
        config.update()
    config.draw(screen)
    pg.time.delay(DELAY)
    pg.display.update()
