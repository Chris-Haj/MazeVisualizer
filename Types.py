import random

from pygame import sprite, Surface
from MazeGen import MazeGen
import numpy as np
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)


class Puzzle:
    def __init__(self, Generator: MazeGen, BlockSize: int):
        Center = lambda number: (number * BlockSize) + (BlockSize // 2)
        self.entities = sprite.Group()
        self.start, self.end = Generator.startPoint, Generator.endPoint
        self.GridStart = [Center(i) for i in Generator.startPoint][::-1]
        self.GridEnd = [Center(i) for i in Generator.endPoint][::-1]

        self.maze = Generator.Board
        self.height, self.width = Generator.Shape

        self.player = Player(self.GridStart, BlockSize - 4, Generator.Shape)
        self.goal = Goal(self.GridEnd, BlockSize - 4)
        self.CenterOfBlocks = np.zeros((self.height, self.width, 2), dtype=int)
        for i in range(self.height):
            for j in range(self.width):
                self.CenterOfBlocks[i][j][0] = Center(j)
                self.CenterOfBlocks[i][j][1] = Center(i)
        self.Walls = np.array([], dtype=Wall)
        self.WallCoords = []
        i = cur = WallCur = 0
        for row in self.maze:
            j = 0
            for block in row:
                if block == 0:
                    self.WallCoords.insert(WallCur, np.array(self.CenterOfBlocks[i][j]))
                    self.Walls = np.append(self.Walls, Wall((self.CenterOfBlocks[i][j]), BlockSize - 4))
                    self.entities.add(self.Walls[cur])
                    cur += 1
                j += 1
                WallCur += 1
            i += 1
        self.entities.add(self.goal)
        self.entities.add(self.player)


class Wall(sprite.Sprite):
    def __init__(self, position: tuple[int, int], BlockSize: int):
        super(Wall, self).__init__()
        self.surf = Surface((BlockSize, BlockSize))
        colors = ['purple']
        index = random.randint(0, len(colors) - 1)
        self.surf.fill(color=colors[index])
        self.rect = self.surf.get_rect(center=position)


class Player(sprite.Sprite):
    def __init__(self, position: tuple[int, int], BlockSize: int, Sizes):
        super(Player, self).__init__()
        self.surf = Surface((BlockSize, BlockSize))
        self.surf.fill(color='white')
        self.rect = self.surf.get_rect(center=position)
        self.jump = BlockSize + 4
        self.height, self.width = Sizes
        self.startingPos = list(position)

    def update(self, pressed, curPos, walls: list, height, width) -> None:
        nextPos = np.array(curPos)
        CanMove = True
        if pressed[K_UP] and curPos[1] != self.jump // 2:
            nextPos[1] -= self.jump
            for wall in walls:
                if np.array_equal(nextPos, wall):
                    CanMove = False
            if CanMove:
                self.rect.move_ip(0, -self.jump)
                curPos[1] -= self.jump
        elif pressed[K_DOWN] and curPos[1] != height - self.jump // 2:
            nextPos[1] += self.jump
            for wall in walls:
                if np.array_equal(nextPos, wall):
                    CanMove = False
            if CanMove:
                curPos[1] += self.jump
                self.rect.move_ip(0, self.jump)
        elif pressed[K_LEFT] and curPos[0] != self.jump // 2:
            nextPos[0] -= self.jump
            for wall in walls:
                if np.array_equal(nextPos, wall):
                    CanMove = False
            if CanMove:
                curPos[0] -= self.jump
                self.rect.move_ip(-self.jump, 0)
        elif pressed[K_RIGHT] and curPos[0] != width - self.jump // 2:
            nextPos[0] += self.jump
            for wall in walls:
                if np.array_equal(nextPos, wall):
                    CanMove = False
            if CanMove:
                curPos[0] += self.jump
                self.rect.move_ip(self.jump, 0)


class Goal(sprite.Sprite):
    def __init__(self, position, BlockSize: int):
        super(Goal, self).__init__()
        self.surf = Surface((BlockSize, BlockSize))
        self.surf.fill(color='deepskyblue')
        self.rect = self.surf.get_rect(center=position)


class Path(sprite.Sprite):
    def __init__(self, position, BlockSize: int):
        super(Goal, self).__init__()
        self.surf = Surface((BlockSize, BlockSize))
        self.surf.fill(color='deepskyblue')
        self.rect = self.surf.get_rect(center=position)
