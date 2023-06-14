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
pygame.display.set_caption("PokePy Test")
player_image: pygame.surface
enemy_image: pygame.surface


def draw_window():
    """draws the window every time"""

    WIN.fill(c.TYPE_GHOST_COLOR)
    draw_sprites()
    pygame.display.update()


def draw_sprites():
    """Draws the player and wild Pokemon sprites"""

    player = pygame.transform.scale(player_image, (c.POKEMON_WIDTH, c.POKEMON_HEIGHT))
    WIN.blit(player, (0, 200))

    enemy = pygame.transform.scale(enemy_image, (c.POKEMON_WIDTH, c.POKEMON_HEIGHT))
    WIN.blit(enemy, (300, 0))


def get_sprite_from_url(url: str) -> pygame.surface:
    """
    Gets a pokemon sprite from a url and returns
    it as a pygame surface.
    """

    img_request = requests.get(url, timeout=3)
    img_data = io.BytesIO(img_request.content)
    img = pygame.image.load(img_data)
    return img


player_data = pokemon.Pokemon(None, 1)
player_image: pygame.surface = get_sprite_from_url(
    player_data.get_sprites().get("back_default")
)

enemy_data = pokemon.Pokemon(None, 4)
enemy_image: pygame.surface = get_sprite_from_url(
    enemy_data.get_sprites().get("front_default")
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
