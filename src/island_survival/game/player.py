"""
Player module for Island Survival text-based adventure game.

This module defines the Player class which represents the game player
and tracks their progress, inventory, and current location.
"""

from typing import List, Optional


class Player:
    """
    Represents the player in the game.
    
    The Player class tracks the player's progress, inventory, current location,
    and other game state information.
    
    Attributes:
        moves (int): Number of moves the player has made
        score (int): Player's current score
        inventory (List[str]): List of items the player is carrying
        name (str): Player's name
        current_location (int): Index of the player's current location
    """
    
    def __init__(self, moves: int, score: int, inventory: List[str], 
                 name: str, current_location: int):
        """
        Initialize a new Player.
        
        Args:
            moves: Number of moves the player has made
            score: Player's current score
            inventory: List of items the player is carrying
            name: Player's name
            current_location: Index of the player's current location
        """
        self.moves = moves
        self.score = score
        self.inventory = inventory
        self.name = name
        self.current_location = current_location
    
    def add_item(self, item: str) -> None:
        """
        Add an item to the player's inventory.
        
        Args:
            item: The item to add to inventory
        """
        if item not in self.inventory:
            self.inventory.append(item)
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the player's inventory.
        
        Args:
            item: The item to remove from inventory
            
        Returns:
            True if item was removed, False if item was not in inventory
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """
        Check if the player has a specific item.
        
        Args:
            item: The item to check for
            
        Returns:
            True if player has the item, False otherwise
        """
        return item in self.inventory
    
    def get_inventory_string(self) -> str:
        """
        Get a formatted string of the player's inventory.
        
        Returns:
            Formatted string of inventory items
        """
        if not self.inventory:
            return "Your inventory is empty."
        return f"{self.name}'s Inventory: {', '.join(self.inventory)}."
    
    def __str__(self) -> str:
        """Return string representation of the player."""
        return f"Player: {self.name} (Score: {self.score}, Moves: {self.moves})"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the player."""
        return (f"Player(name='{self.name}', score={self.score}, "
                f"moves={self.moves}, location={self.current_location}, "
                f"inventory={self.inventory})")
