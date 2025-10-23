# Island Survival - Text-Based Adventure Game

**Author:** Jake Tantorski  
**Course:** CMPT 120L  
**Date:** December 4, 2017

## Overview

Island Survival is a text-based adventure game where players must navigate an island, collect survival items, and reach safety before time runs out. The game features multiple locations, item collection, and strategic decision-making.

## Game Objective

Your goal is to survive on the island by:
1. Collecting essential survival items (spear, wood, water)
2. Navigating to the cave with all required items
3. Avoiding death by drowning or running out of time

## How to Play

### Setup
1. Make sure you have Python 3.6+ installed
2. Run the game: `python project.py`

### Game Controls

| Command | Description |
|---------|-------------|
| `north`, `south`, `east`, `west` | Move in the specified direction |
| `look` | Examine your current location |
| `search` | Search for items at your location |
| `take <item>` | Pick up a specific item (after searching) |
| `drop <item>` | Drop an item at your current location |
| `use <item>` | Use an item (context-dependent) |
| `inventory` | View your current items |
| `map` | View the island map (if you have one) |
| `pray` | Get a hint (can only be used once) |
| `points` | Check your current score |
| `help` | Show available commands |
| `quit` | Exit the game |

### Game Locations

The island contains 12 unique locations:
- **Beach** - Starting location with a lifevest
- **Rocks** - Barren rocky area
- **Cave** - Your ultimate destination (win condition)
- **Forest** - Contains wood (use axe to collect)
- **Field** - Contains a map
- **Village** - Contains a spear
- **Hills** - Rolling hills with eagles
- **River** - Dangerous crossing (requires lifevest)
- **Marsh** - Contains an axe
- **Waterfall** - Contains a canteen
- **Dam** - Contains logs (use axe to collect)
- **Pond** - Contains water (use canteen to collect)

### Winning Conditions

You win by reaching the **Cave** with all three survival items:
- **Spear** (weapon)
- **Wood** (firewood)
- **Water** (hydration)

### Losing Conditions

- **Drowning**: Attempting to cross the river without a lifevest
- **Time Limit**: Taking more than 69 moves
- **Quitting**: Using the quit command

### Tips for Success

1. **Start by collecting the lifevest** at the beach
2. **Get the map** from the field to navigate efficiently
3. **Use the axe** at the forest to get dry wood
4. **Use the canteen** at the pond to get water
5. **Collect the spear** from the village
6. **Navigate to the cave** with all items to win

## Technical Details

### File Structure
```
CMPT120-Project/
├── src/
│   └── island_survival/
│       ├── __init__.py
│       ├── game/
│       │   ├── __init__.py
│       │   ├── game_engine.py    # Main game logic and state management
│       │   ├── game_locale.py    # Location class
│       │   └── player.py         # Player class and inventory
│       ├── data/
│       │   ├── __init__.py
│       │   ├── constants.py      # Game constants and settings
│       │   └── world.py          # World map and location data
│       └── utils/
│           ├── __init__.py
│           ├── display.py        # Display and output functions
│           └── input_handler.py # Input parsing and validation
├── main.py                       # Main entry point
├── setup.py                      # Package setup
├── requirements.txt              # Dependencies
└── README.md                     # This documentation
```

### Legacy Files (Deprecated)
- `project.py` - Original monolithic game file (kept for reference)
- `player.py` - Original player class (moved to src/)
- `gameLocale.py` - Original location class (moved to src/)

### Key Features
- Object-oriented design with separate classes for Player and GameLocale
- Comprehensive error handling and input validation
- Modular function design for easy maintenance
- Type hints for better code clarity
- Detailed documentation and comments

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Running the Game

### Option 1: Super Simple (Recommended)
```bash
python3 run_game.py
```

### Option 2: Run the new modular version
```bash
python3 main.py
```

### Option 3: Run the original version
```bash
python3 project.py
```

### Option 4: Install as a package (Advanced)
If you want to install the package system-wide, you'll need to use a virtual environment:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Install the package
pip install -e .

# Run the game
python main.py
# OR
island-survival

# Deactivate when done
deactivate
```

**Note:** For most users, simply running `python3 main.py` is the easiest option!

## Game Rules

1. You start at the beach with no items
2. Each location can only be visited once for full points
3. Some items require specific tools to collect (axe for wood, canteen for water)
4. The river is dangerous without a lifevest
5. You have a limited number of moves (69) to complete the game
6. The pray command can only be used once per game

## Credits

**Developer:** Jake Tantorski  
**Email:** jake.tantorski1@marist.edu  
**Course:** CMPT 120L - Computer Science I Lab

---

*Good luck surviving the island!*
