import pygame as pg
from chars import *
import Maze as mz


def PrepareCoords() -> list[25]:
    """
    returns a list of coordinates for the grid
    """
    Multiplier = HEIGHT // DIM
    coords = [[(j * Multiplier + 50, i * Multiplier + 50) for j in range(DIM)] for i in range(DIM)]
    return coords



def main() -> None:
    pg.init()
    screen = pg.display.set_mode((WIDTH + 1, HEIGHT + 1))
    puzzle = mz.Puzzle()
    player = Player((150, 150))
    Coords = PrepareCoords()
    walls = drawWalls(Coords, puzzle.maze)
    mainLoop(screen, player, walls)


def drawWalls(Coords: list[25], maze: list):
    cur = i = j = 0
    walls = [] * GRID
    for row in maze:
        for block in row:
            if block == 0:
                walls.insert(cur, Wall(Coords[i][j]))
                cur += 1
            j += 1
        i += 1
        j = 0
    return walls


def drawGrid(screen: pg.display) -> None:
    for i in range(0, WIDTH + 100, SIZE_OF_OBJECT[0]):
        pg.draw.line(screen, color='white', start_pos=(i, 0), end_pos=(i, HEIGHT))
        pg.draw.line(screen, color='white', start_pos=(0, i), end_pos=(HEIGHT, i))


def mainLoop(screen: pg.display, player: Player, walls) -> None:
    running = True
    clock = pg.time.Clock()
    FPS = 20

    while running:
        clock.tick(FPS)

        for event in pg.event.get():

            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False

        screen.fill(color='black')
        drawGrid(screen)
        for wall in walls:
            screen.blit(wall.surf,wall.rect)
        pg.display.update()


if __name__ == '__main__':
    main()
