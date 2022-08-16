from Types import *
from MazeGen import MazeGen
import pygame as pg


def setUp():

    HEIGHT, WIDTH = 400, 400
    BlockSize = 100
    ColDim = HEIGHT // BlockSize
    RowDim = WIDTH // BlockSize
    HEIGHT, WIDTH = HEIGHT + BlockSize, WIDTH + BlockSize

    Generator = MazeGen(ColDim, RowDim)
    puzzle = Puzzle(Generator, BlockSize)
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    mainLoop(screen, puzzle.player, puzzle.entities, puzzle.WallCoords, HEIGHT, WIDTH, BlockSize)


def drawGrid(screen: pg.display, WIDTH, HEIGHT, SIZE) -> None:
    for i in range(0, WIDTH + 100, SIZE):
        pg.draw.line(screen, color='white', start_pos=(i, 0), end_pos=(i, HEIGHT))
        pg.draw.line(screen, color='white', start_pos=(0, i), end_pos=(HEIGHT, i))


def Animate(screen, clock, entities, FPS, color):
    steroids = 12
    running = True
    group = sprite.Group()
    for i in entities:
        clock.tick(FPS * steroids)
        for event in pg.event.get():

            if event.type == QUIT:
                running = False
        if not running:
            break
        screen.fill(color=color)
        for j in group:
            screen.blit(j.surf, j.rect)
        group.add(i)
        pg.display.update()


def mainLoop(screen, player, entities, walls, h, w, size):
    running = True
    color = 'black'
    clock = pg.time.Clock()
    FPS = 15
    curPos = player.startingPos
    pressed = None
    Animate(screen, clock, entities, FPS, color)
    pressed = pg.key.get_pressed()
    while running:
        clock.tick(FPS)

        for event in pg.event.get():

            pressed = pg.key.get_pressed()

            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        screen.fill(color=color)
        drawGrid(screen, h, w, size)
        for entity in entities:
            screen.blit(entity.surf, entity.rect)
        player.update(pressed, curPos, walls, h, w)
        pg.display.update()


if __name__ == '__main__':
    setUp()
