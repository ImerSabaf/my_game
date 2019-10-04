"""
Character class which represent all the
attributes ands method for an Character
"""


class Character:
    """
    Character class
    """

    def __init__(self, name):
        self.name = name
        self.level = 1

    def info(self):
        """
        return information for this character
        """
        return "{} is level :[{}]".format(self.name, self.level)
