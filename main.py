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
player_data: pokemon.Pokemon
enemy_image: pygame.surface
enemy_data: pokemon.Pokemon


def draw_window():
    """draws the window every time"""

    WIN.fill(c.BLUE)
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


def change_pokemon_by_string(pokemon_name: str, sprite_name: str):
    """
    returns new pokemon class data and image based on the string inputs. Used to change
    pokemon by using their name and what sprite is desired.
    """

    data: pokemon.Pokemon = pokemon.Pokemon(pokemon_name)
    image: pygame.surface = get_sprite_from_url(data.get_sprites().get(sprite_name))
    return data, image


def change_pokemon_by_id(pokemon_id: int, sprite_name: str):
    """
    returns new pokemon class data and image based on pokemon id and sprite string. Used to change
    pokemon by using their pokedex id number and what sprite is desired.
    """

    data: pokemon.Pokemon = pokemon.Pokemon(0, pokemon_id)
    image: pygame.surface = get_sprite_from_url(data.get_sprites().get(sprite_name))
    return data, image


player_data, player_image = change_pokemon_by_id(94, "back_default")
enemy_data, enemy_image = change_pokemon_by_string("nidorino", "front_default")


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
