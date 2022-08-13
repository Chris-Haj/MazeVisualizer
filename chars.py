from pygame import sprite, Surface
import random as ra
from Maze import N
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    QUIT
)

LENGTH = 100
DIM = N
WIDTH, HEIGHT = DIM * LENGTH, DIM * LENGTH
GRID = DIM * DIM
SIZE_OF_OBJECT = (WIDTH // DIM, HEIGHT // DIM)


class Wall(sprite.Sprite):
    def __init__(self, position: tuple[int, int]):
        super(Wall, self).__init__()
        self.surf = Surface(tuple(SIZE_OF_OBJECT[i] - 4 for i in range(2)))
        self.surf.fill(color='grey')
        self.rect = self.surf.get_rect(center=position)


class Player(sprite.Sprite):
    def __init__(self, position: tuple[int, int]):
        super(Player, self).__init__()
        self.surf = Surface(tuple(SIZE_OF_OBJECT[i] - 4 for i in range(2)))
        self.surf.fill(color='white')
        self.rect = self.surf.get_rect(center=position)
        self.jump = SIZE_OF_OBJECT[0]

    def update(self, pressed, curPos,walls) -> None:
        nextPos = curPos[::]
        if pressed[K_UP] and (curPos[1]-self.jump) not in walls and curPos[1] != self.jump//2:
            nextPos[1] -= self.jump
            if nextPos not in walls:
                self.rect.move_ip(0, -self.jump)
                curPos[1] -= self.jump
        elif pressed[K_DOWN] and (curPos[1] + self.jump) not in walls and curPos[1] != HEIGHT - self.jump//2:
            nextPos[1] += self.jump
            if nextPos not in walls:
                curPos[1] += self.jump
                self.rect.move_ip(0, self.jump)
        elif pressed[K_LEFT] and (curPos[0] - self.jump) not in walls and curPos[0] != self.jump//2:
            nextPos[0] -= self.jump
            if nextPos not in walls:
                curPos[0] -= self.jump
                self.rect.move_ip(-self.jump, 0)
        elif pressed[K_RIGHT] and (curPos[0] + self.jump) not in walls and curPos[0] != WIDTH - self.jump//2:
            nextPos[0] += self.jump
            if nextPos not in walls:
                curPos[0] += self.jump
                self.rect.move_ip(self.jump, 0)

class Goal(sprite.Sprite):
    def __init__(self, position):
        super(Goal, self).__init__()
        self.surf = Surface(tuple(SIZE_OF_OBJECT[i] - 4 for i in range(2)))
        self.surf.fill(color='yellow')
        self.rect = self.surf.get_rect(center=position)
