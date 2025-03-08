#!/usr/bin/env python3
"""
treasureIsland.py - A text-based adventure game.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/08
License: MIT
Dependencies: None (built-in functions only)

Description:
This script is a simple interactive adventure game where the player
must make choices to find a hidden treasure. At each step, the player
is presented with multiple options, and selecting the wrong one
results in death, while the correct choices lead further into the
adventure until the treasure is found.

The script takes user input as a string representing their choice
and provides output indicating whether they continue, win, or lose.

Usage:
Run the script and follow the prompts:
    python treasureIsland.py

Example Output:
    You are at a crossroad. Where do you want to go? Left or Right: left
    You come to a lake. Do you swim or wait for a boat? wait
    You reach an island with three doors. Which one do you choose? Red, Blue, or Yellow: yellow
    Congratulations! You found the treasure!
"""

# Treasure Island - A simple text-based adventure game

# Ask the player to make the first decision at a crossroad
decision = input("You are at a crossroad. Where do you want to go? Left or Right: ")

# Convert input to uppercase for case-insensitive comparison
if decision.upper() == "LEFT":
    # Player encounters a lake and must choose to swim or wait
    decision = input("You come to a lake. Do you swim or wait for a boat?: ")

    if decision.upper() == "WAIT":
        # Player reaches an island with three doors and must choose one
        decision = input("You reach an island with three doors. Which one do you choose? Red, Blue, or Yellow: ")

        if decision.upper() == "YELLOW":
            print("Congratulations! You found the treasure!")
        #Wrong decision tree
        elif decision.upper() == "BLUE":
            print("Sorry! You ended up in a cave with a bear.")
        elif decision.upper() == "RED":
            print("Sorry! You ended up in a raptor's nest.")
        else:
            print("Sorry! You must work on your spelling.")
    else:
        print("Sorry! You got eaten by saltwater piranhas.")
else:
    print("Sorry! You fell down a cliff.")