# 🏝️ Island Survival - Text-Based Adventure Game

**Author:** Jake Tantorski  
**Course:** CMPT 120L - Computer Science I Lab  
**Date:** December 4, 2017  
**Version:** 2.0.0 (Modular Refactor)

---

## 📖 Overview

Island Survival is an immersive text-based adventure game where players must navigate a mysterious island, collect essential survival items, and reach safety before time runs out. The game features 12 unique locations, strategic item collection, and multiple paths to victory.

### 🎯 Game Objective

Your mission is to survive on the island by:
1. **Collecting essential survival items** (spear, wood, water)
2. **Navigating to the cave** with all required items
3. **Avoiding death** by drowning or running out of time
4. **Exploring the island** to understand its layout

---

## 🚀 Quick Start

### **Super Simple (Recommended)**
```bash
python3 run_game.py
```

### **Alternative Methods**
```bash
# Modular version
python3 main.py

# Original version (legacy)
python3 project.py
```

---

## 🎮 How to Play

### **Game Controls**

| Command | Description | Example |
|---------|-------------|---------|
| `north`, `south`, `east`, `west` | Move in directions | `north` |
| `look` | Examine current location | `look` |
| `search` | Search for items | `search` |
| `take <item>` | Pick up specific item | `take map` |
| `drop <item>` | Drop an item | `drop spear` |
| `use <item>` | Use an item | `use axe` |
| `inventory` | View your items | `inventory` |
| `map` | Show island map (if you have one) | `map` |
| `pray` | Get a hint (once per game) | `pray` |
| `points` | Check your score | `points` |
| `help` | Show all commands | `help` |
| `quit` | Exit the game | `quit` |

### **Game Locations**

The island contains 12 unique locations to explore:

| Location | Description | Items Available |
|----------|-------------|-----------------|
| **🏖️ Beach** | Starting location with waves and palm trees | `lifevest` |
| **🪨 Rocks** | Barren rocky surface with no life | None |
| **🕳️ Cave** | Your ultimate destination (win condition) | None |
| **🌲 Forest** | Thick forest with tall trees | `wood` (use axe) |
| **🌾 Field** | Lush grassy field with rodents | `map` |
| **🏘️ Village** | Old village with dying fire | `spear` |
| **⛰️ Hills** | Rolling hills with eagles flying | None |
| **🌊 River** | Dangerous river crossing | None |
| **🌿 Marsh** | Marsh with ducks and beavers | `axe` |
| **💧 Waterfall** | Beautiful waterfall with spray | `canteen` |
| **🪵 Dam** | Beaver-constructed dam | `logs` (use axe) |
| **🐟 Pond** | Crystal clear pond with fish | `water` (use canteen) |

### **Winning Conditions**

You win by reaching the **🕳️ Cave** with all three survival items:
- **🗡️ Spear** (weapon for protection)
- **🪵 Wood** (firewood for warmth)
- **💧 Water** (hydration for survival)

### **Losing Conditions**

- **💀 Drowning**: Attempting to cross the river without a lifevest
- **⏰ Time Limit**: Taking more than 69 moves
- **🚪 Quitting**: Using the quit command

---

## 🗺️ Island Map

```
Hills------ Rocks--------Cave
  |           |            | 
  |           |            | 
  |           |            | 
Field------ Beach--------Forest
     \        |            | 
      \       |            | 
       \      |            | 
        \---Village-----River
              |            | 
              |            | 
              |            | 
            Marsh-----Waterfall
              |            | 
              |            | 
              |            | 
            Dam----------Pond
```

---

## 🎯 Strategy Guide

### **Optimal Path to Victory**

1. **🏖️ Start at Beach** - Collect the `lifevest`
2. **🌾 Go to Field** - Get the `map` for navigation
3. **🏘️ Visit Village** - Collect the `spear`
4. **🌿 Go to Marsh** - Get the `axe`
5. **🌲 Use axe at Forest** - Get dry `wood`
6. **💧 Go to Waterfall** - Get the `canteen`
7. **🐟 Use canteen at Pond** - Get `water`
8. **🕳️ Navigate to Cave** - Win the game!

### **Pro Tips**

- **🗺️ Get the map early** - It shows all connections between locations
- **🦺 Keep the lifevest** - You'll need it to cross the river safely
- **⏰ Plan your moves** - You have 69 moves total
- **🙏 Use pray once** - Get a helpful hint when stuck
- **🔍 Always search first** - Before taking items

---

## 🏗️ Technical Architecture

### **Project Structure**

```
CMPT120-Project/
├── 📁 src/island_survival/          # Main package
│   ├── 📁 game/                     # Core game logic
│   │   ├── game_engine.py          # Main game state management
│   │   ├── game_locale.py          # Location class
│   │   └── player.py               # Player class & inventory
│   ├── 📁 data/                     # Game data & constants
│   │   ├── constants.py            # All game constants
│   │   └── world.py                # World map & locations
│   └── 📁 utils/                    # Utility functions
│       ├── display.py              # Display & output functions
│       └── input_handler.py        # Input parsing & validation
├── main.py                          # New modular entry point
├── run_game.py                      # Super simple launcher
├── setup.py                         # Package installation
├── requirements.txt                 # Dependencies
├── README.md                        # This documentation
└── [Legacy files preserved]         # project.py, player.py, gameLocale.py
```

### **Key Features**

- **🏗️ Modular Architecture**: Clean separation of concerns
- **📝 Type Hints**: Full type annotations for better code clarity
- **🔧 Error Handling**: Robust input validation and error recovery
- **📚 Documentation**: Comprehensive docstrings and comments
- **🎮 Multiple Entry Points**: Various ways to run the game
- **🔄 Backward Compatibility**: Original files preserved

---

## 🛠️ Development

### **Requirements**

- **Python 3.6+** (No external dependencies required)
- **Cross-platform** (Windows, macOS, Linux)

### **Installation Options**

#### **Option 1: Direct Run (Recommended)**
```bash
python3 run_game.py
```

#### **Option 2: Modular Version**
```bash
python3 main.py
```

#### **Option 3: Legacy Version**
```bash
python3 project.py
```

#### **Option 4: Package Installation (Advanced)**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Install package
pip install -e .

# Run game
python main.py
# OR
island-survival

# Deactivate when done
deactivate
```

---

## 🎮 Game Rules

1. **🏁 Starting Point**: You begin at the beach with no items
2. **📍 Location Scoring**: Each new location gives 5 points
3. **🔍 Search First**: You must search before taking items
4. **🛠️ Tool Requirements**: Some items need specific tools to collect
5. **🌊 River Danger**: The river requires a lifevest to cross safely
6. **⏰ Move Limit**: You have 69 moves to complete the game
7. **🙏 Prayer Limit**: The pray command can only be used once
8. **🔄 Restart Option**: You can play multiple games in one session

---

## 🐛 Troubleshooting

### **Common Issues**

**Q: The map command doesn't work**
- A: Make sure you have the map in your inventory (`inventory` command)
- A: You need to `search` first, then `take map` at the field

**Q: I can't take items**
- A: You must `search` the location first before taking items
- A: Some items require using tools first (axe for wood, canteen for water)

**Q: I drowned in the river**
- A: You need a `lifevest` to cross the river safely
- A: Get the lifevest from the beach at the start

**Q: The game ends immediately**
- A: This was a bug in the original version - the modular version fixes this
- A: Use `python3 run_game.py` for the fixed version

### **Getting Help**

- **In-game**: Type `help` for command list
- **Hints**: Type `pray` once per game for guidance
- **Navigation**: Type `map` to see the island layout
- **Status**: Type `points` to check your score

---

## 📊 Game Statistics

- **🎯 Total Locations**: 12 unique areas to explore
- **🎒 Collectible Items**: 8 different items
- **⏱️ Time Limit**: 69 moves maximum
- **🏆 Win Conditions**: 1 (reach cave with all items)
- **💀 Lose Conditions**: 3 (drowning, timeout, quit)
- **🗺️ Map Locations**: All 12 locations connected

---

## 🏆 Achievements

- **🏖️ Beach Walker**: Visit the beach
- **🗺️ Cartographer**: Get the map
- **🦺 Life Saver**: Collect the lifevest
- **🗡️ Warrior**: Get the spear
- **🪵 Lumberjack**: Collect wood with axe
- **💧 Hydrated**: Get water with canteen
- **🏆 Survivor**: Win the game!

---

## 📝 License & Credits

**Developer:** Jake Tantorski  
**Email:** jake.tantorski1@marist.edu  
**Course:** CMPT 120L - Computer Science I Lab  
**Institution:** Marist College  

**Version History:**
- **v1.0.0** - Original monolithic version
- **v2.0.0** - Modular refactor with enhanced features

---

## 🤝 Contributing

This is an academic project, but suggestions for improvements are welcome:

1. **🐛 Bug Reports**: Report issues you encounter
2. **💡 Feature Ideas**: Suggest new game mechanics
3. **📚 Documentation**: Help improve this README
4. **🎮 Testing**: Try different strategies and report findings

---

## 🎉 Enjoy Your Adventure!

Good luck surviving the island! Remember:
- **🗺️ Plan your route** with the map
- **⏰ Watch your moves** - you have 69 total
- **🛠️ Use tools wisely** - axe for wood, canteen for water
- **🌊 Stay safe** - don't cross the river without a lifevest
- **🏆 Collect everything** - spear, wood, and water for victory!

**Happy exploring! 🏝️⚔️**