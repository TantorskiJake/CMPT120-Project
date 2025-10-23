#!/usr/bin/env python3
"""
Development setup script for Island Survival.

This script helps set up the development environment and run various tasks.
"""

import sys
import os
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and print the result."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ {description} failed")
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ {description} failed with error: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("❌ Python 3.6+ is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def setup_development_environment():
    """Set up the development environment."""
    print("🏗️ Setting up Island Survival development environment...")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Add src to path for imports
    src_path = Path(__file__).parent.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    # Test imports
    print("\n🧪 Testing imports...")
    try:
        from island_survival.game import GameEngine
        from island_survival.data import create_locations
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    
    # Test game initialization
    print("\n🎮 Testing game initialization...")
    try:
        engine = GameEngine()
        locations = create_locations()
        engine.initialize_locations(locations)
        print("✅ Game engine initializes correctly")
    except Exception as e:
        print(f"❌ Game initialization failed: {e}")
        return False
    
    print("\n🎉 Development environment setup complete!")
    return True

def run_tests():
    """Run the test suite."""
    print("\n🧪 Running tests...")
    return run_command("python3 -m pytest tests/ -v", "Test suite")

def run_game():
    """Run the game."""
    print("\n🎮 Starting Island Survival...")
    return run_command("python3 scripts/run_game.py", "Game launch")

def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/dev_setup.py [setup|test|game|all]")
        print("\nOptions:")
        print("  setup  - Set up development environment")
        print("  test   - Run test suite")
        print("  game   - Run the game")
        print("  all    - Run all tasks")
        return
    
    command = sys.argv[1].lower()
    
    if command == "setup":
        setup_development_environment()
    elif command == "test":
        run_tests()
    elif command == "game":
        run_game()
    elif command == "all":
        setup_development_environment()
        run_tests()
        run_game()
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
