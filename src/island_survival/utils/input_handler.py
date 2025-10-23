"""
Input handling utilities for Island Survival.

This module handles player input parsing and validation.
"""

from typing import Tuple
from ..data.constants import COMMANDS


def get_next_command() -> Tuple[int, str]:
    """
    Get the next command from the player.
    
    Returns:
        Tuple[int, str]: The command index and item name (if specified)
    """
    while True:
        try:
            choice = input("Command: ").strip().split(" ")
            cmd = choice[0].lower()
            
            # Get the item if specified
            try:
                cmd_item = choice[1].lower()
            except IndexError:
                cmd_item = ""
            
            # Find the command in the list
            if cmd in COMMANDS:
                return COMMANDS.index(cmd), cmd_item
            else:
                print("That's not a valid command! Type 'help' for available commands.")
                
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
