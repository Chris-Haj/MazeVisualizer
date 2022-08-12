import pygame as pg
from chars import *

pg.init()



def mainLoop(screen: pg.display) -> None:
    running = True
    clock = pg.time.Clock()
    FPS = 60
    while running:
        clock.tick(FPS)
        pressed = pg.key.get_pressed()

        for event in pg.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                enemy = Wall()
                enemies.add(enemy)
                all_sprites.add(enemy)

        player.update(pressed)
        enemies.update()
        if pg.sprite.spritecollideany(player, enemies):
            surfaces = (player.surf.get_width() + 3, player.surf.get_height() + 3)
            # player.surf = pg.transform.scale(player.surf, surfaces)
            print(player.rect.height, player.rect.width)
            player.rect.inflate_ip(surfaces)
        screen.fill(color='black')
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pg.display.update()


def main() -> None:
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    mainLoop(screen)


if __name__ == '__main__':
    main()
