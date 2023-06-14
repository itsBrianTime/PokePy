""" Pokemon Type testing with pygame"""

import io
import pygame
import pygame.image
import requests
import constants as c
import pokemon


# TODO: Design Idea. Keep pokemon class as a pokemon generator. but then make a class
# that can have a pokemon object. so I can make the User pokemon and Wild pokemon. just use
# the generator class to change them if needed.

WIN = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Type Test")
gengar_image: pygame.surface
nido_image: pygame.surface


def draw_window():
    """draws the window every time"""
    WIN.fill(c.WHITE)
    draw_sprites()
    # pygame.display.flip()
    pygame.display.update()


def draw_sprites():
    """Draws the player and wild Pokemon sprites"""
    gengar = pygame.transform.scale(gengar_image, (c.POKEMON_WIDTH, c.POKEMON_HEIGHT))
    WIN.blit(gengar, (0, 200))
    nidorino = pygame.transform.scale(nido_image, (c.POKEMON_WIDTH, c.POKEMON_HEIGHT))
    WIN.blit(nidorino, (300, 0))


def get_sprite_from_url(url: str) -> pygame.surface:
    """
    Gets a pokemon sprite from a url and returns
    it as a pygame surface.
    """
    img_request = requests.get(url, timeout=3)
    img_data = io.BytesIO(img_request.content)
    img = pygame.image.load(img_data)
    return img


gengar_data = pokemon.Pokemon("gengar")
# print(gengar_data.get_sprites())
gengar_image: pygame.surface = get_sprite_from_url(
    gengar_data.get_sprites().get("back_default")
)

nido_data = pokemon.Pokemon("nidoking")
nido_image: pygame.surface = get_sprite_from_url(
    nido_data.get_sprites().get("front_default")
)


def main():
    """begins pygame and handles all input"""
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(c.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()
    raise SystemExit


if __name__ == "__main__":
    main()
