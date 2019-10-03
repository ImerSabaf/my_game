"""
Player class which represent all the
attributes ands method for the player
"""


class Player:
    """
    player class
    """

    def __init__(self, name):
        self.name = name
        self.level = 1

    def info(self):
        """
        return information for this player
        """
        return "{} is level :[{}]".format(self.name, self.level)
