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

SIZE_OF_OBJECT = (50, 50)
WIDTH, HEIGHT = 1920, 1080
player_width, player_height = 50, 50


class Enemy(sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = Surface(SIZE_OF_OBJECT)
        self.surf.fill(color='red')
        self.rect = self.surf.get_rect(
            center=(
                WIDTH,
                ra.randint(0, HEIGHT)
            )
        )
        self.speed = ra.randint(5, 15)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.kill()


class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((player_width, player_height))
        self.surf.fill(color='white')
        self.rect = self.surf.get_rect()

    def update(self, pressed):
        if pressed[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
