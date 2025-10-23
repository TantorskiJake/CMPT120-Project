"""
Display utilities for Island Survival.

This module handles all display-related functions including
location descriptions, maps, help text, and game endings.
"""

from typing import List
from ..game.player import Player
from ..game.game_locale import GameLocale
from ..data.constants import *


def print_location(place: int, locations: List[GameLocale]) -> None:
    """
    Print the location description based on whether the player has been there before.
    
    Args:
        place: Location index to print
        locations: List of all game locations
    """
    location = locations[place]
    
    if not location.been_there:
        print(location.loc)
        # Note: Score increment should be handled by the game engine
        location.been_there = True
    else:
        print(location.short_loc)


def draw_map(player: Player) -> None:
    """
    Display the island map if the player has one.
    
    Args:
        player: The current player object
    """
    if player.has_item("map"):
        print("Hills------ Rocks--------Cave")
        print("  |           |            | ")
        print("  |           |            | ")
        print("  |           |            | ")
        print("Field------ Beach--------Forest")
        print("     \\        |            | ")
        print("      \\       |            | ")
        print("       \\      |            | ")
        print("        \\---Village-----River")
        print("              |            | ")
        print("              |            | ")
        print("              |            | ")
        print("            Marsh-----Waterfall")
        print("              |            | ")
        print("              |            | ")
        print("              |            | ")
        print("            Dam----------Pond")
    else:
        print("You do not have a map with you.")


def display_help() -> None:
    """Display the help information with available commands."""
    print("Commands are:")
    print("- North, South, East, West - Move in those directions")
    print("- Quit - End the game")
    print("- Look - Look around the current location")
    print("- Map - Access the map (if you have one)")
    print("- Search - Search for items at the current location")
    print("- Take <item> - Take a specific item after searching")
    print("- Drop <item> - Drop a specific item")
    print("- Use <item> - Use a specific item")
    print("- Inventory - Show your inventory")
    print("- Pray - Get a hint (can only be used once)")
    print("- Points - Show your current score")
    print("- Help - Show this help message")


def display_ending(ending: int, player: Player) -> None:
    """
    Display the appropriate ending message based on how the game ended.
    
    Args:
        ending: The ending type (0=win, 1=timeout, 2=drowned, 3=explored)
        player: The player object
    """
    if ending == 0:
        print(f"{player.name} wins! You have successfully made it to a safe location with a weapon, firewood and water to spend the night.")
    elif ending == 1:
        print("You took too long and got caught in the cold of the night. You died. GAME OVER!")
    elif ending == 2:
        print("You did not have something to keep you afloat as you tried to cross and you drowned. GAME OVER!")
    elif ending == 3:
        print("You have been everywhere and you have the map with you. You have seen the island and can survive and navigate!")
    else:
        print("Thanks for playing!")


def display_intro(player_name: str) -> None:
    """
    Display the game introduction and instructions.
    
    Args:
        player_name: The player's name
    """
    print()
    print("Island Survival is a text-based adventure game.")
    print("Controls: North, South, East, West, Help, Points, Search, Take, Map, Use, Pray, and Quit.")
    print(f"On this adventure {player_name} will enter into many locations.")
    print("Hopefully you can make it out alive.")
    print()
    print("You have awoken on a sandy shore with a seagull staring you right in the face.")
    print("You rub your eyes and look around. You do not remember anything except your name:")
    print(f"{player_name} and a few other basic skills.")
    print("Unsure of what to do you start looking around.")
    print()


def get_player_name() -> str:
    """
    Get the player's name and return it.
    
    Returns:
        str: The player's name
    """
    print("WELCOME TO ISLAND SURVIVAL!")
    name = input("Enter your name: ").strip()
    if not name:
        name = "Adventurer"
    return name


def ask_restart() -> bool:
    """
    Ask the player if they want to play again.
    
    Returns:
        bool: True if player wants to restart, False otherwise
    """
    while True:
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if restart == "yes":
            return True
        elif restart == "no":
            print("Thanks for playing!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")
