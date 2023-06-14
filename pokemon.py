""" Holds single pokemon data """

from typing import Dict, Iterable, List
from dataclasses import dataclass
import requests
import constants as c


@dataclass(slots=True)
class Pokemon:
    """Holds pokemon name and id for looking up different resources about the pokemon"""

    name: str
    id: int
    url: str

    def __init__(self, name: str = None, id: int = None) -> None:
        if name and id:
            self.name = name
            self.id = id
            self.url = c.POKE_API_URL + name
        elif name:
            self.name = name
            self.url = c.POKE_API_URL + name
            self.id = requests.get(self.url, timeout=3).json()["id"]
        elif id:
            self.id = id
            self.url = c.POKE_API_URL + str(id)
            self.name = requests.get(self.url, timeout=3).json()["name"]
            self.url = c.POKE_API_URL + self.name
        elif name is None and id is None:
            raise TypeError("You must provide either a name or a id!")
        elif name == "":
            raise ValueError("Name cannot be an empty string.")
        elif id == 0:
            raise ValueError("id cannot be zero.")

    def get_abilities(self) -> List:
        """Gets a list of abilities this Pokémon could potentially have."""
        return requests.get(self.url, timeout=3).json()["abilities"]

    def get_ability_names(self) -> List:
        """Gets a list names of abilities this Pokémon could potentially have."""
        return [
            d["ability"]["name"]
            for d in requests.get(self.url, timeout=3).json()["abilities"]
        ]

    def get_base_experience(self) -> int:
        """get the base experience gained for defeating this Pokémon."""
        return requests.get(self.url, timeout=3).json()["base_experience"]

    def get_forms(self) -> List:
        """Get a list of forms this Pokémon can take on."""
        return requests.get(self.url, timeout=3).json()["forms"]

    def get_game_indices(self) -> List:
        """Get a list of game indices relevant to Pokémon item by generation."""
        return requests.get(self.url, timeout=3).json()["game_indices"]

    def get_held_items(self) -> List:
        """Get a list of items this Pokémon may be holding when encountered."""
        return requests.get(self.url, timeout=3).json()["held_items"]

    def get_height(self) -> int:
        """Get the height of this Pokémon in decimeters."""
        return requests.get(self.url, timeout=3).json()["height"]

    def weight(self) -> int:
        """Get the weight of this Pokémon in hectograms."""
        return requests.get(self.url, timeout=3).json()["weight"]

    def get_id(self) -> int:
        """The identifier for the pokemon resource."""
        return self.id

    def get_moves(self) -> List:
        """Get A list of moves along with learn methods and level details pertaining to specific version groups."""
        return requests.get(self.url, timeout=3).json()["moves"]

    def get_move_by_number(self, number: str) -> Dict:
        """Get a move based on the its id number"""
        return requests.get(
            self.url.replace("pokemon", "move").replace(self.name, str(number)),
            timeout=3,
        ).json()

    def get_move_names(self, numbers: Iterable) -> List:
        """Get a list of move names for the Pokemon"""
        return [move["name"] for move in [self.get_move_by_number(n) for n in numbers]]

    def get_move_by_name(self, name: str) -> Dict:
        """Get a move by using its name"""
        return {
            d["move"]["name"]: d["move"]
            for d in requests.get(self.url, timeout=3).json()["moves"]
        }[name]

    def get_order(self) -> int:
        """Order for sorting. Almost national order, except families are grouped together."""
        return requests.get(self.url, timeout=3).json()["order"]

    def get_sprites(self) -> Dict:
        """Get a set of sprites used to depict this Pokémon in the game"""
        return requests.get(self.url, timeout=3).json()["sprites"]

    def get_stats(self) -> List:
        """Get a list of base stat values for this Pokémon."""
        return requests.get(self.url, timeout=3).json()["stats"]

    def get_types(self) -> List:
        """Get a list of details showing types this Pokémon has."""
        return requests.get(self.url, timeout=3).json()["types"]
