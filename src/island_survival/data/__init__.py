"""
Data module for Island Survival.

This module contains game data, constants, and world configuration.
"""

from .constants import *
from .world import create_locations, get_location, WORLD_MAP

__all__ = ['create_locations', 'get_location', 'WORLD_MAP']
