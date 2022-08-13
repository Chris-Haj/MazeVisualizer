import pygame as pg
from chars import *
import Maze as mz

Multiplier = HEIGHT // DIM
Coords = [[(j * Multiplier + 50, i * Multiplier + 50) for j in range(DIM)] for i in range(DIM)]
WallCoords = []


def main() -> None:
    pg.init()
    screen = pg.display.set_mode((WIDTH + 1, HEIGHT + 1))
    puzzle = mz.Puzzle()
    start = puzzle.start[::-1]
    start = [start[i] * Multiplier + 50 for i in range(2)]
    end = puzzle.end[::-1]
    end = [end[i] * Multiplier + 50 for i in range(2)]
    player = Player(tuple(start))
    goal = Goal(tuple(end))
    walls = drawWalls(Coords, puzzle.maze)
    mainLoop(screen, player, walls, goal, start, end)


def drawWalls(Coords: list, maze: list) -> list:
    cur = i = j = 0
    walls = [] * GRID
    for row in maze:
        for block in row:
            if block == 0:
                walls.insert(cur, Wall(Coords[i][j]))
                WallCoords.insert(cur, list(Coords[i][j]))
                cur += 1
            j += 1
        i += 1
        j = 0
    return walls


def drawGrid(screen: pg.display) -> None:
    for i in range(0, WIDTH + 100, SIZE_OF_OBJECT[0]):
        pg.draw.line(screen, color='white', start_pos=(i, 0), end_pos=(i, HEIGHT))
        pg.draw.line(screen, color='white', start_pos=(0, i), end_pos=(HEIGHT, i))


def mainLoop(screen: pg.display, player: Player, walls, goal, curPos, end) -> None:
    running = True
    clock = pg.time.Clock()
    FPS = 10
    group = pg.sprite.Group()
    allBlocks = pg.sprite.Group()
    for wall in walls:
        group.add(wall)
        allBlocks.add(wall)
    allBlocks.add(goal)
    allBlocks.add(player)
    frames = 0
    while  running:
        clock.tick(FPS)
        frames+=1
        for event in pg.event.get():

            pressed = pg.key.get_pressed()

            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False

        screen.fill(color='black')
        drawGrid(screen)
        for block in allBlocks:
            screen.blit(block.surf, block.rect)
        player.update(pressed,curPos,WallCoords)
        pg.display.update()


if __name__ == '__main__':
    main()