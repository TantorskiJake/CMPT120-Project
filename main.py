"""
Main entry point for Island Survival.

This is the main entry point for the Island Survival text-based adventure game.
It initializes the game engine and runs the main game loop.
"""

import sys
from src.island_survival.game import GameEngine
from src.island_survival.data import create_locations
from src.island_survival.utils import (
    get_player_name, display_intro, display_ending, ask_restart
)


def main() -> None:
    """
    Main game function that runs the complete game loop.
    """
    # Initialize game engine
    game_engine = GameEngine()
    
    # Create and initialize locations
    locations = create_locations()
    game_engine.initialize_locations(locations)
    
    # Get player name and display intro
    player_name = get_player_name()
    game_engine.player.name = player_name
    display_intro(player_name)
    
    # Run the main game loop
    game_engine.run_game()
    
    # Display ending
    display_ending(game_engine.ending, game_engine.player)
    
    # Ask if player wants to restart
    while ask_restart():
        # Clear screen for new game
        print("\n" * 50)
        print("Resetting Game...")
        print("\n" * 30)
        
        # Reset game state
        game_engine.reset_game()
        
        # Get new player name
        player_name = get_player_name()
        game_engine.player.name = player_name
        display_intro(player_name)
        
        # Run the game again
        game_engine.run_game()
        display_ending(game_engine.ending, game_engine.player)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
    finally:
        print("Copyright: Jake Tantorski jake.tantorski1@marist.edu")
