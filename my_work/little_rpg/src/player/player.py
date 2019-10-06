"""
Player class which represent all the
attributes ands method for the player
"""

from little_rpg.src.character.character import Character


class Player:
    """
    player class
    """

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.characters = []
        self.characters.append(Character("Clone Sergeant"))

    def info(self):
        """
        return information for this player
        """
        return "{} is level :[{}]".format(self.name, self.level)

    def print_character_info(self):
        """
        print list characters info for this player
        """
        for the_char in self.characters:
            print(the_char.name)
