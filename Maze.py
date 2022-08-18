from Types import *
from MazeGen import MazeGen
import pygame as pg
from pygame.locals import (
    K_r,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    K_s,
    QUIT
)
from solver import solveMaze
from SearchAlgro import SearchAlgo

createAnotherGame = True


def setUp() -> None:
    global createAnotherGame
    while createAnotherGame:
        createAnotherGame = False
        HEIGHT, WIDTH = 800, 1800
        BlockSize: int = 50
        ColDim: int = HEIGHT // BlockSize
        RowDim: int = WIDTH // BlockSize
        HEIGHT, WIDTH = HEIGHT + BlockSize, WIDTH + BlockSize
        Generator: MazeGen = MazeGen(ColDim, RowDim)
        puzzle: Puzzle = Puzzle(Generator, BlockSize)
        screen: pg.display = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
        mainLoop(screen, puzzle, HEIGHT, WIDTH, BlockSize)


def mainLoop(screen: pg.display, puzzle: Puzzle, h: int, w: int, size: int) -> None:
    global createAnotherGame
    running: bool = True
    Grid: bool = False
    color: str = 'black'
    clock: pg.time.Clock = pg.time.Clock()
    FPS: int = 20
    curPos: list = puzzle.player.startingPos
    Animate(screen, clock, puzzle.entities, FPS, color)
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
                if event.key == K_SPACE:
                    Grid = not Grid
                if event.key == K_r:
                    createAnotherGame = True
                    running = False
                if event.key == K_s:
                    solveMaze(puzzle.maze, h, w, curPos, puzzle.GridEnd)

        screen.fill(color=color)
        if Grid:
            drawGrid(screen, h, w, size)
        for entity in puzzle.entities:
            screen.blit(entity.surf, entity.rect)
        puzzle.player.update(pressed, curPos, puzzle.WallCoords, h, w)
        pg.display.update()


def drawGrid(screen: pg.display, HEIGHT: int, WIDTH: int, SIZE: int) -> None:
    for i in range(0, WIDTH + 100, SIZE):
        pg.draw.line(screen, color='white', start_pos=(i, 0), end_pos=(i, HEIGHT))
    for i in range(0, HEIGHT + 100, SIZE):
        pg.draw.line(screen, color='white', start_pos=(0, i), end_pos=(WIDTH, i))


def Animate(screen: pg.display, clock: pg.time.Clock, entities: pg.sprite.Sprite, FPS: int, color: str) -> None:
    steroids = 12
    running = True
    group = sprite.Group()
    for i in entities:
        clock.tick(FPS * steroids)
        for event in pg.event.get():

            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        if not running:
            break
        screen.fill(color=color)
        for j in group:
            screen.blit(j.surf, j.rect)
        group.add(i)
        pg.display.update()


if __name__ == '__main__':
    setUp()
