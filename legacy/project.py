"""
Island Survival - A Text-Based Adventure Game
Author: Jake Tantorski
Course: CMPT 120L
Date: 12/4/17

A text-based adventure game where the player must survive on an island
by collecting items, exploring locations, and making strategic decisions.
The goal is to reach the cave with the necessary survival items.
"""

from player import Player
from gameLocale import GameLocale
from typing import List, Optional, Tuple
import sys

# Global game state variables
userAction: int = 0
ending: int = 0
cmdItem: str = ""
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
COMMANDS = ["north", "south", "east", "west", "quit", "look", "map", 
           "search", "take", "help", "points", "drop", "use", "inventory", "pray"]
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
# Initialize the player
userPlayer = Player(0, 0, [], "name", BEACH)
# Game locations - each location has a name, description, short description, 
# and whether it has been visited/examined, plus any items present
LOCATIONS = [
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
def get_player_name() -> None:
    """
    Get the player's name and set it in the player object.
    """
    print("WELCOME TO ISLAND SURVIVAL!")
    userPlayer.name = input("Enter your name: ").strip()
    if not userPlayer.name:
        userPlayer.name = "Adventurer"


def display_intro() -> None:
    """
    Display the game introduction and instructions.
    """
    print()
    print("Island Survival is a text-based adventure game.")
    print("Controls: North, South, East, West, Help, Points, Search, Take, Map, Use, Pray, and Quit.")
    print(f"On this adventure {userPlayer.name} will enter into many locations.")
    print("Hopefully you can make it out alive.")
    print()
    print("You have awoken on a sandy shore with a seagull staring you right in the face.")
    print("You rub your eyes and look around. You do not remember anything except your name:")
    print(f"{userPlayer.name} and a few other basic skills.")
    print("Unsure of what to do you start looking around.")
    print()
def main() -> None:
    """
    Main game function that runs the complete game loop.
    """
    get_player_name()
    display_intro()
    run_game()
    display_ending()
    ask_restart()
def run_game() -> None:
    """
    Main game loop that handles player input and game logic.
    """
    global userAction, ending, cmdItem
    
    # Game state variables
    prayers = 1
    use_axe = 2
    ending = 99
    use_river = 1
    
    print_location(userPlayer.current_location)
    
    while True:
        # Check for game ending conditions
        if ending == 2:  # Player drowned
            break
        elif userPlayer.moves == 69:  # Too many moves
            ending = 1
            break
        elif ending == 0:  # Player won
            break
        elif userPlayer.score == 60 and "map" in userPlayer.inventory:
            ending = 3  # Player completed exploration
            break
        
        # Special river crossing event
        elif use_river == 1 and userPlayer.current_location == RIVER:
            print("You fall into the river and don't remember how to swim. You have to be quick. What do you use?")
            userAction = get_next_command()
            if userAction == USE and cmdItem == "lifevest" and "lifevest" in userPlayer.inventory:
                print("That was a smart move to use the lifevest. You now know that you need it in order to cross the river.")
                use_river = 0
            else:
                ending = 2
                break
        
        # Axe durability check
        elif use_axe == 0 and "axe" in userPlayer.inventory:
            userPlayer.remove_item("axe")
            print("The axe broke from using it too much.")
        
        # Normal game turn
        else:
            userAction = get_next_command()
            
            if userAction == QUIT:
                break
            elif userAction == LOOK:
                print(LOCATIONS[userPlayer.current_location].loc)
            elif userAction == MAP:
                draw_map()
            elif userAction == SEARCH:
                search_for_item(userPlayer.current_location)
            elif userAction == TAKE:
                take_item(userPlayer.current_location)
            elif userAction == DROP:
                drop_item(userPlayer.current_location)
            elif userAction == USE:
                use_item(userPlayer.current_location)
            elif userAction == INVENTORY:
                print(userPlayer.get_inventory_string())
            elif userAction == HELP:
                display_help()
            elif userAction == POINTS:
                print(f"Score: {userPlayer.score}.")
            elif userAction == PRAY:
                prayer()
            else:
                # Movement command
                userPlayer.current_location = get_location(userPlayer.current_location, userAction)
                print_location(userPlayer.current_location)
                userPlayer.moves += 1
def display_ending() -> None:
    """
    Display the appropriate ending message based on how the game ended.
    """
    global ending
    
    if ending == 0:
        print(f"{userPlayer.name} wins! You have successfully made it to a safe location with a weapon, firewood and water to spend the night.")
    elif ending == 1:
        print("You took too long and got caught in the cold of the night. You died. GAME OVER!")
    elif ending == 2:
        print("You did not have something to keep you afloat as you tried to cross and you drowned. GAME OVER!")
    elif ending == 3:
        print("You have been everywhere and you have the map with you. You have seen the island and can survive and navigate!")
    else:
        print("Thanks for playing!")
def get_next_command() -> int:
    """
    Get the next command from the player.
    
    Returns:
        int: The command index from the COMMANDS list
    """
    global cmdItem
    
    while True:
        try:
            choice = input("Command: ").strip().split(" ")
            cmd = choice[0].lower()
            
            # Get the item if specified
            try:
                cmdItem = choice[1].lower()
            except IndexError:
                cmdItem = ""
            
            # Find the command in the list
            if cmd in COMMANDS:
                return COMMANDS.index(cmd)
            else:
                print("That's not a valid command! Type 'help' for available commands.")
                
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")        
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


def print_location(place: int) -> None:
    """
    Print the location description based on whether the player has been there before.
    
    Args:
        place: Location index to print
    """
    location = LOCATIONS[place]
    
    if not location.been_there:
        print(location.loc)
        userPlayer.score += 5
        location.been_there = True
    else:
        if userAction != LOOK:
            print(location.short_loc)            
def search_for_item(place: int) -> None:
    """
    Search for items at the current location.
    
    Args:
        place: Location index to search
    """
    userPlayer.moves += 1
    LOCATIONS[place].exam_there = True
    
    if LOCATIONS[place].items is not None:
        print(f"Look! A(n) {LOCATIONS[place].items}")
    else:
        print("Nothing here.")


def take_item(place: int) -> None:
    """
    Take an item from the current location.
    
    Args:
        place: Location index to take item from
    """
    userPlayer.moves += 1
    
    if not LOCATIONS[place].exam_there:
        print("You need to search for an item first!")
        return
    
    if LOCATIONS[place].items is None:
        print("I guess there is nothing here.")
        return
    
    if cmdItem == "":
        print("You need to take a specific item.")
        return
    
    if cmdItem == LOCATIONS[place].items:
        # Special locations that require using an item first
        if userPlayer.current_location in [FOREST, DAM, POND]:
            print("You need to use a specific item here to take it.")
        else:
            userPlayer.add_item(LOCATIONS[place].items)
            print(f"Congratulations! You took a {LOCATIONS[place].items}.")
            LOCATIONS[place].items = None
    else:
        print("That item is not here.")
def drop_item(place: int) -> None:
    """
    Drop an item at the current location.
    
    Args:
        place: Location index to drop item at
    """
    userPlayer.moves += 1
    
    if cmdItem == "":
        print("You need to drop a specific item.")
        return
    
    if userPlayer.has_item(cmdItem):
        if LOCATIONS[place].items is not None:
            print("There is already an item at this location.")
        else:
            userPlayer.remove_item(cmdItem)
            print(f"You dropped a {cmdItem}.")
            LOCATIONS[place].items = cmdItem
    else:
        print("That item is not in your inventory.")
def use_item(place: int) -> None:
    """
    Use an item at the current location.
    
    Args:
        place: Location index to use item at
    """
    global ending
    
    userPlayer.moves += 1
    
    if cmdItem == "":
        print("You need to use a specific item.")
        return
    
    if not userPlayer.has_item(cmdItem):
        print("You do not have that item.")
        return
    
    # Check for winning condition (cave with all survival items)
    if place == CAVE and userPlayer.has_item("spear") and userPlayer.has_item("wood") and userPlayer.has_item("water"):
        ending = 0
        return
    
    # Forest: use axe to get wood
    elif place == FOREST and userPlayer.has_item("axe"):
        print("You got dry wood to make a fire.")
        userPlayer.add_item("wood")
        LOCATIONS[place].items = None
    
    # Dam: use axe to get logs (but they're wet)
    elif place == DAM and userPlayer.has_item("axe"):
        print("You got wet logs. That won't help make a fire.")
        userPlayer.add_item("logs")
        LOCATIONS[place].items = None
    
    # Pond: use canteen to get water
    elif place == POND and userPlayer.has_item("canteen"):
        print("You got water.")
        userPlayer.add_item("water")
        LOCATIONS[place].items = None
    
    else:
        print("You can't use that item here.")
def draw_map() -> None:
    """
    Display the island map if the player has one.
    """
    if userPlayer.has_item("map"):
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

def ask_restart() -> None:
    """
    Ask the player if they want to play again and reset the game if yes.
    """
    while True:
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if restart == "yes":
            reset_game()
            main()
            break
        elif restart == "no":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Please enter 'yes' or 'no'.")


def reset_game() -> None:
    """
    Reset the game state to start a new game.
    """
    # Reset player values
    userPlayer.inventory = []
    userPlayer.score = 0
    userPlayer.moves = 0
    userPlayer.current_location = BEACH
    userPlayer.name = ""
    
    # Reset all locations
    for place in LOCATIONS:
        place.been_there = False
        place.exam_there = False
        place.items = None
    
    # Restore initial items
    LOCATIONS[BEACH].items = "lifevest"
    LOCATIONS[FOREST].items = "wood"
    LOCATIONS[FIELD].items = "map"
    LOCATIONS[VILLAGE].items = "spear"
    LOCATIONS[MARSH].items = "axe"
    LOCATIONS[WATERFALL].items = "canteen"
    LOCATIONS[DAM].items = "logs"
    LOCATIONS[POND].items = "water"
    
    # Clear screen for new game
    print("\n" * 50)
    print("Resetting Game...")
    print("\n" * 30)
def prayer() -> None:
    """
    Provide a hint to the player based on their current situation.
    Can only be used once per game.
    """
    global prayers
    
    if prayers == 1:
        if userPlayer.has_item("map"):
            print("The air swirls around you and a ghostly figure appears.")
            print("He says to you in a low wispy voice: Cave...Safety. The air becomes dead and he disappears.")
        elif not userPlayer.has_item("lifevest"):
            print("The air swirls around you and a ghostly figure appears.")
            print("He says to you in a low wispy voice: Do not drown in the river. The air becomes dead and he disappears.")
        else:
            print("The air swirls around you and a ghostly figure appears.")
            print("He says to you in a low wispy voice: The field will bring you in the right direction. The air becomes dead and he disappears.")
        prayers -= 1
    else:
        print("You already prayed.")


def display_help() -> None:
    """
    Display the help information with available commands.
    """
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


if __name__ == "__main__":
    main()
    print("Copyright: Jake Tantorski jake.tantorski1@marist.edu")
