"""
Game engine for Island Survival.

This module contains the main game logic, state management, and game loop.
"""

from typing import List, Optional
from .player import Player
from .game_locale import GameLocale
from ..data.constants import *
from ..data.world import WORLD_MAP
from ..utils.input_handler import get_next_command
from ..utils.display import print_location, draw_map, display_help, display_ending


class GameEngine:
    """
    Main game engine that manages the game state and logic.
    """
    
    def __init__(self):
        """Initialize the game engine."""
        self.player = Player(0, 0, [], "name", BEACH)
        self.locations: List[GameLocale] = []
        self.ending = 99  # Initialize to non-winning state
        self.prayers = 1
        self.use_axe = 2
        self.use_river = 1
        self.cmd_item = ""
    
    def _get_location(self, current_location: int, direction: int) -> int:
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
    
    def initialize_locations(self, locations: List[GameLocale]) -> None:
        """
        Initialize the game locations.
        
        Args:
            locations: List of GameLocale objects
        """
        self.locations = locations
    
    def run_game(self) -> None:
        """
        Main game loop that handles player input and game logic.
        """
        print_location(self.player.current_location, self.locations)
        
        while True:
            # Check for game ending conditions
            if self.ending == 2:  # Player drowned
                break
            elif self.player.moves == MAX_MOVES:  # Too many moves
                self.ending = 1
                break
            elif self.ending == 0:  # Player won
                break
            elif self.player.score == WINNING_SCORE and "map" in self.player.inventory:
                self.ending = 3  # Player completed exploration
                break
            
            # Special river crossing event
            elif self.use_river == 1 and self.player.current_location == RIVER:
                print("You fall into the river and don't remember how to swim. You have to be quick. What do you use?")
                user_action, self.cmd_item = get_next_command()
                if user_action == USE and self.cmd_item == "lifevest" and "lifevest" in self.player.inventory:
                    print("That was a smart move to use the lifevest. You now know that you need it in order to cross the river.")
                    self.use_river = 0
                else:
                    self.ending = 2
                    break
            
            # Axe durability check
            elif self.use_axe == 0 and "axe" in self.player.inventory:
                self.player.remove_item("axe")
                print("The axe broke from using it too much.")
            
            # Normal game turn
            else:
                user_action, self.cmd_item = get_next_command()
                
                if user_action == QUIT:
                    break
                elif user_action == LOOK:
                    print(self.locations[self.player.current_location].loc)
                elif user_action == MAP:
                    draw_map(self.player)
                elif user_action == SEARCH:
                    self._search_for_item()
                elif user_action == TAKE:
                    self._take_item()
                elif user_action == DROP:
                    self._drop_item()
                elif user_action == USE:
                    self._use_item()
                elif user_action == INVENTORY:
                    print(self.player.get_inventory_string())
                elif user_action == HELP:
                    display_help()
                elif user_action == POINTS:
                    print(f"Score: {self.player.score}.")
                elif user_action == PRAY:
                    self._prayer()
                else:
                    # Movement command
                    self.player.current_location = self._get_location(self.player.current_location, user_action)
                    print_location(self.player.current_location, self.locations)
                    self.player.moves += 1
    
    def _search_for_item(self) -> None:
        """Search for items at the current location."""
        self.player.moves += 1
        self.locations[self.player.current_location].exam_there = True
        
        if self.locations[self.player.current_location].items is not None:
            print(f"Look! A(n) {self.locations[self.player.current_location].items}")
        else:
            print("Nothing here.")
    
    def _take_item(self) -> None:
        """Take an item from the current location."""
        self.player.moves += 1
        
        if not self.locations[self.player.current_location].exam_there:
            print("You need to search for an item first!")
            return
        
        if self.locations[self.player.current_location].items is None:
            print("I guess there is nothing here.")
            return
        
        if self.cmd_item == "":
            print("You need to take a specific item.")
            return
        
        if self.cmd_item == self.locations[self.player.current_location].items:
            # Special locations that require using an item first
            if self.player.current_location in [FOREST, DAM, POND]:
                print("You need to use a specific item here to take it.")
            else:
                self.player.add_item(self.locations[self.player.current_location].items)
                print(f"Congratulations! You took a {self.locations[self.player.current_location].items}.")
                self.locations[self.player.current_location].items = None
        else:
            print("That item is not here.")
    
    def _drop_item(self) -> None:
        """Drop an item at the current location."""
        self.player.moves += 1
        
        if self.cmd_item == "":
            print("You need to drop a specific item.")
            return
        
        if self.player.has_item(self.cmd_item):
            if self.locations[self.player.current_location].items is not None:
                print("There is already an item at this location.")
            else:
                self.player.remove_item(self.cmd_item)
                print(f"You dropped a {self.cmd_item}.")
                self.locations[self.player.current_location].items = self.cmd_item
        else:
            print("That item is not in your inventory.")
    
    def _use_item(self) -> None:
        """Use an item at the current location."""
        self.player.moves += 1
        
        if self.cmd_item == "":
            print("You need to use a specific item.")
            return
        
        if not self.player.has_item(self.cmd_item):
            print("You do not have that item.")
            return
        
        # Check for winning condition (cave with all survival items)
        if (self.player.current_location == CAVE and 
            self.player.has_item("spear") and 
            self.player.has_item("wood") and 
            self.player.has_item("water")):
            self.ending = 0
            return
        
        # Forest: use axe to get wood
        elif self.player.current_location == FOREST and self.player.has_item("axe"):
            print("You got dry wood to make a fire.")
            self.player.add_item("wood")
            self.use_axe -= 1
            self.locations[self.player.current_location].items = None
        
        # Dam: use axe to get logs (but they're wet)
        elif self.player.current_location == DAM and self.player.has_item("axe"):
            print("You got wet logs. That won't help make a fire.")
            self.player.add_item("logs")
            self.use_axe -= 1
            self.locations[self.player.current_location].items = None
        
        # Pond: use canteen to get water
        elif self.player.current_location == POND and self.player.has_item("canteen"):
            print("You got water.")
            self.player.add_item("water")
            self.locations[self.player.current_location].items = None
        
        else:
            print("You can't use that item here.")
    
    def _prayer(self) -> None:
        """Provide a hint to the player based on their current situation."""
        if self.prayers == 1:
            if self.player.has_item("map"):
                print("The air swirls around you and a ghostly figure appears.")
                print("He says to you in a low wispy voice: Cave...Safety. The air becomes dead and he disappears.")
            elif not self.player.has_item("lifevest"):
                print("The air swirls around you and a ghostly figure appears.")
                print("He says to you in a low wispy voice: Do not drown in the river. The air becomes dead and he disappears.")
            else:
                print("The air swirls around you and a ghostly figure appears.")
                print("He says to you in a low wispy voice: The field will bring you in the right direction. The air becomes dead and he disappears.")
            self.prayers -= 1
        else:
            print("You already prayed.")
    
    def reset_game(self) -> None:
        """Reset the game state to start a new game."""
        # Reset player values
        self.player.inventory = []
        self.player.score = 0
        self.player.moves = 0
        self.player.current_location = BEACH
        self.player.name = ""
        
        # Reset all locations
        for place in self.locations:
            place.been_there = False
            place.exam_there = False
            place.items = None
        
        # Restore initial items
        self.locations[BEACH].items = "lifevest"
        self.locations[FOREST].items = "wood"
        self.locations[FIELD].items = "map"
        self.locations[VILLAGE].items = "spear"
        self.locations[MARSH].items = "axe"
        self.locations[WATERFALL].items = "canteen"
        self.locations[DAM].items = "logs"
        self.locations[POND].items = "water"
        
        # Reset game state
        self.ending = 99
        self.prayers = 1
        self.use_axe = 2
        self.use_river = 1
