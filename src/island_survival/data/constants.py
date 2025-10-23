"""
Game constants and configuration for Island Survival.

This module contains all the constants used throughout the game,
including location indices, command mappings, and game settings.
"""

# Location constants - indices for the world map
BEACH = 0
ROCKS = 1
CAVE = 2
FOREST = 3
FIELD = 4
VILLAGE = 5
HILLS = 6
RIVER = 7
MARSH = 8
WATERFALL = 9
DAM = 10
POND = 11

# Command constants
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
QUIT = 4
LOOK = 5
MAP = 6
SEARCH = 7
TAKE = 8
HELP = 9
POINTS = 10
DROP = 11
USE = 12
INVENTORY = 13
PRAY = 14

# Available commands
COMMANDS = [
    "north", "south", "east", "west", "quit", "look", "map", 
    "search", "take", "help", "points", "drop", "use", "inventory", "pray"
]

# Game settings
MAX_MOVES = 69
WINNING_SCORE = 60
PRAYERS_ALLOWED = 1
AXE_USES = 2

# Location names for display
LOCATION_NAMES = [
    "Beach", "Rocks", "Cave", "Forest", "Field", "Village",
    "Hills", "River", "Marsh", "Waterfall", "Dam", "Pond"
]
