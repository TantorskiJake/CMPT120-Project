"""
GameLocale module for Island Survival text-based adventure game.

This module defines the GameLocale class which represents different locations
in the game world that the player can visit.
"""

from typing import Optional


class GameLocale:
    """
    Represents a location in the game world.
    
    Each GameLocale object contains information about a specific location
    including its name, description, whether the player has visited it,
    whether it has been examined, and any items present.
    
    Attributes:
        name (str): The name of the location
        loc (str): Full description of the location (shown on first visit)
        short_loc (str): Short description (shown on subsequent visits)
        been_there (bool): Whether the player has visited this location
        exam_there (bool): Whether the player has examined this location
        items (Optional[str]): Item present at this location, None if no item
    """
    
    def __init__(self, name: str, loc: str, short_loc: str, 
                 been_there: bool, exam_there: bool, items: Optional[str]):
        """
        Initialize a new GameLocale.
        
        Args:
            name: The name of the location
            loc: Full description of the location
            short_loc: Short description for return visits
            been_there: Whether the player has visited this location
            exam_there: Whether the player has examined this location
            items: Item present at this location (None if no item)
        """
        self.name = name
        self.loc = loc
        self.short_loc = short_loc
        self.been_there = been_there
        self.exam_there = exam_there
        self.items = items
    
    def __str__(self) -> str:
        """Return string representation of the location."""
        return f"Location: {self.name}"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the location."""
        return (f"GameLocale(name='{self.name}', been_there={self.been_there}, "
                f"exam_there={self.exam_there}, items={self.items})")
