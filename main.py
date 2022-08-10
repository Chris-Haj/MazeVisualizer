import pygame as pg
from chars import *

player = Player()
enemies = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_sprites.add(player)


def mainLoop(screen):
    running = True
    clock = pg.time.Clock()
    while running:
        clock.tick(60)
        pressed = pg.key.get_pressed()

        for event in pg.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False

        player.update(pressed)
        screen.fill(color='black')
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pg.display.update()


def main():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    mainLoop(screen)


if __name__ == '__main__':
    main()
