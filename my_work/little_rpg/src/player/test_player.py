"""
Test file for the player class
"""

from player import Player


def test_instance_info():
    """
    test an instance a player and the
    info method
    """
    player_test = Player("test_name")
    assert player_test.info() == "test_name is level :[1]"
    assert player_test.level == 1


def test_print_character_info():
    """
    TO DO
    """
    player_test = Player("test_name")
    player_test.print_character_info()
    assert player_test.level == 1
