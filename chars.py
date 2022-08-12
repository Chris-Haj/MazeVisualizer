from pygame import sprite, Surface
import random as ra
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

WIDTH, HEIGHT = 500, 500
DIM = 5
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

    def update(self, pressed) -> None:
        if pressed[K_UP]:
            self.rect.move_ip(0, SIZE_OF_OBJECT[0])
        if pressed[K_DOWN]:
            self.rect.move_ip(0, SIZE_OF_OBJECT[0])
        if pressed[K_LEFT]:
            self.rect.move_ip(-SIZE_OF_OBJECT[0], 0)
        if pressed[K_RIGHT]:
            self.rect.move_ip(SIZE_OF_OBJECT[0], 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Goal(sprite.Sprite):
    def __init__(self, position):
        super(Goal, self).__init__()
        self.surf = Surface(tuple(SIZE_OF_OBJECT[i] - 4 for i in range(2)))
        self.surf.fill(color='yellow')
        self.rect = self.surf.get_rect(center=position)
