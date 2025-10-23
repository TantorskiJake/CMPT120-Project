"""
World map and location data for Island Survival.

This module contains the world map structure and initial location data.
"""

from typing import List, Optional
from .constants import *
from ..game.game_locale import GameLocale


# World map - 2D array representing connections between locations
# Format: [North, South, East, West] for each location
WORLD_MAP = [
    [ROCKS, VILLAGE, FOREST, FIELD],      # BEACH
    [None, BEACH, CAVE, HILLS],          # ROCKS
    [None, FOREST, None, ROCKS],          # CAVE
    [CAVE, RIVER, None, BEACH],           # FOREST
    [HILLS, VILLAGE, BEACH, None],        # FIELD
    [BEACH, MARSH, RIVER, FIELD],         # VILLAGE
    [None, FIELD, ROCKS, None],          # HILLS
    [FOREST, WATERFALL, None, VILLAGE],   # RIVER
    [VILLAGE, DAM, WATERFALL, None],      # MARSH
    [RIVER, POND, None, MARSH],           # WATERFALL
    [MARSH, None, POND, None],            # DAM
    [WATERFALL, None, None, DAM]          # POND
]


def create_locations() -> List[GameLocale]:
    """
    Create and return the initial game locations with their descriptions and items.
    
    Returns:
        List[GameLocale]: List of all game locations
    """
    return [
        # BEACH
        GameLocale("beach", 
                   "A beach appears. Waves crash against the sandy beach and palm trees sway in the wind.", 
                   "You are at the beach.", 
                   False, False, "lifevest"),
        
        # ROCKS  
        GameLocale("rocks", 
                   "You stumble upon a rocky surface. There is no life to be seen and water is scarce.", 
                   "You are at the rocks.", 
                   False, False, None),
        
        # CAVE
        GameLocale("cave", 
                   "Between some bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back.", 
                   "You are at the cave.", 
                   False, False, None),
        
        # FOREST
        GameLocale("forest", 
                   "A thick forest appears with many tall looming trees. Animals are abundant and you smell pine.", 
                   "You are at the forest.", 
                   False, False, "wood"),
        
        # FIELD
        GameLocale("field", 
                   "Now a lush grassy field is in your sights. The grass is untouched except for the small rodents that live in it. Flies buzz around your head in the heat.", 
                   "You are at the field.", 
                   False, False, "map"),
        
        # VILLAGE
        GameLocale("village", 
                   "You can make out what seems to be an old village. A fire is almost out and spears are lying around.", 
                   "You are at the village.", 
                   False, False, "spear"),
        
        # HILLS
        GameLocale("hills", 
                   "As the sun glares in your eyes you see that the hills in front of you are rolling everywhere. Grass is covering the hills and an eagle flies above.", 
                   "You are at the hills.", 
                   False, False, None),
        
        # RIVER
        GameLocale("river", 
                   "Water is rushing past you and you gaze upon a giant river. Swimming through seems to be your only way of crossing.", 
                   "You are at the river.", 
                   False, False, None),
        
        # MARSH
        GameLocale("marsh", 
                   "You stumble upon a marsh and see ducks flying around and a beaver creating a dam.", 
                   "You are at the marsh.", 
                   False, False, "axe"),
        
        # WATERFALL
        GameLocale("waterfall", 
                   "A beautiful waterfall comes into sight and the water sprays your face. You stare into the beauty that is water falling from a cliff and listen to it crash onto the rocks below.", 
                   "You are at the waterfall.", 
                   False, False, "canteen"),
        
        # DAM
        GameLocale("dam", 
                   "A group of beavers is visible and they are constructing a dam. The dam is blocking the water from running freely.", 
                   "You are at the dam.", 
                   False, False, "logs"),
        
        # POND
        GameLocale("pond", 
                   "There appears to be a crystal clear pond with a pair of fish swimming side by side.", 
                   "You are at the pond.", 
                   False, False, "water")
    ]


def get_location(current_location: int, direction: int) -> int:
    """
    Get the new location based on the current location and direction.
    
    Args:
        current_location: Current location index
        direction: Direction to move (NORTH, SOUTH, EAST, WEST)
        
    Returns:
        int: New location index
    """
    if WORLD_MAP[current_location][direction] is None:
        print("There is nothing in that direction.")
        return current_location
    else:
        return WORLD_MAP[current_location][direction]
