# 🏝️ Island Survival - Text-Based Adventure Game

**Author:** Jake Tantorski  
**Course:** CMPT 120L - Computer Science I Lab  
**Date:** December 4, 2017  
**Version:** 2.0.0 (Modular Refactor)

---

## 🚀 Quick Start

### **Super Simple (Recommended)**
```bash
python3 scripts/run_game.py
```

### **Alternative Methods**
```bash
# Modular version
python3 main.py

# Legacy version
python3 legacy/project.py
```

---

## 📁 Project Structure

```
CMPT120-Project/
├── 📚 docs/                          # Documentation
│   ├── README.md                     # Detailed documentation
│   ├── PROJECT_SUMMARY.md            # Project overview
│   └── CHANGELOG.md                  # Version history
├── 🎮 src/island_survival/           # Main source code
│   ├── game/                         # Core game logic
│   ├── data/                         # Game data & constants
│   └── utils/                        # Utility functions
├── 🖼️ assets/                        # Game assets
│   └── ProjectMap.png                # Island map image
├── 📜 legacy/                        # Original files (preserved)
│   ├── project.py                    # Original monolithic game
│   ├── player.py                     # Original player class
│   └── gameLocale.py                 # Original location class
├── 🛠️ scripts/                       # Utility scripts
│   └── run_game.py                   # Simple launcher
├── 🧪 tests/                         # Test files (future)
├── main.py                           # Modular entry point
├── setup.py                          # Package installation
└── requirements.txt                  # Dependencies
```

---

## 🎮 How to Play

### **Game Controls**
- `north`, `south`, `east`, `west` - Move in directions
- `look` - Examine current location
- `search` - Search for items
- `take <item>` - Pick up specific item
- `use <item>` - Use an item
- `inventory` - View your items
- `map` - Show island map (if you have one)
- `help` - Show all commands
- `quit` - Exit the game

### **Game Objective**
Collect essential survival items (spear, wood, water) and reach the cave to win!

### **Winning Conditions**
- Reach the **🕳️ Cave** with all three survival items:
  - **🗡️ Spear** (weapon)
  - **🪵 Wood** (firewood) 
  - **💧 Water** (hydration)

---

## 🏗️ Technical Details

### **Requirements**
- Python 3.6+ (No external dependencies)

### **Architecture**
- **Modular design** with clean separation of concerns
- **Object-oriented structure** with proper class responsibilities
- **Type hints** throughout the codebase
- **Comprehensive documentation** with examples

### **Key Features**
- ✅ **Zero breaking changes** - all original functionality preserved
- ✅ **Enhanced error handling** and input validation
- ✅ **Professional documentation** with comprehensive guides
- ✅ **Multiple entry points** for different user preferences
- ✅ **Clean code structure** following Python best practices

---

## 📚 Documentation

- **[Detailed README](docs/README.md)** - Complete game guide and technical details
- **[Project Summary](docs/PROJECT_SUMMARY.md)** - Project overview and statistics
- **[Changelog](docs/CHANGELOG.md)** - Version history and improvements

---

## 🎯 Quick Commands

```bash
# Run the game (recommended)
python3 scripts/run_game.py

# Run modular version
python3 main.py

# Run original version
python3 legacy/project.py

# Install as package (advanced)
pip install -e .
```

---

## 🏆 Features

- **12 unique locations** to explore
- **8 collectible items** with strategic usage
- **Interactive map system** for navigation
- **Hint system** (pray command)
- **Score tracking** and move counting
- **Multiple win/lose conditions**
- **Restart functionality**

---

## 🤝 Contributing

This is an academic project, but suggestions are welcome:
- 🐛 Bug reports
- 💡 Feature ideas
- 📚 Documentation improvements
- 🎮 Testing and feedback

---

## 📄 License & Credits

**Developer:** Jake Tantorski  
**Email:** jake.tantorski1@marist.edu  
**Course:** CMPT 120L - Computer Science I Lab  
**Institution:** Marist College  

---

## 🎉 Enjoy Your Adventure!

Good luck surviving the island! Remember to plan your route, collect all items, and reach the cave safely.

**Happy exploring! 🏝️⚔️**
