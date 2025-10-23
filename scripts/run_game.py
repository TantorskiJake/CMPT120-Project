#!/usr/bin/env python3
"""
Simple launcher script for Island Survival.

This script automatically sets up the Python path and runs the game.
No installation required!
"""

import sys
import os

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# Import and run the main function
if __name__ == "__main__":
    try:
        from main import main
        main()
    except ImportError as e:
        print(f"Error: Could not import the game modules. {e}")
        print("Make sure you're running this from the project directory.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
