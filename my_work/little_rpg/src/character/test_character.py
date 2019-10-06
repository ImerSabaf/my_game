"""
Test file for the character class
"""

from character import Character


def test_instance_info():
    """
    test an instance a player and the
    info method
    """
    character_test = Character("test_character")
    assert character_test.info() == "test_character is level :[1]"
    assert character_test.level == 1
