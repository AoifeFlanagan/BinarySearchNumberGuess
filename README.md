# Binary Search Number Guessing Game
Repository for a number guessing game, created with python.

## Table of Contents
* [Introduction](https://github.com/AoifeFlanagan/BinarySearchNumberGuess#Introduction)
* [Features](https://github.com/AoifeFlanagan/BinarySearchNumberGuess#Features)
* [Modules](https://github.com/AoifeFlanagan/BinarySearchNumberGuess#Modules)
* [Recommended Interactive Development Environment (IDE)](https://github.com/AoifeFlanagan/BinarySearchNumberGuess#recommended-interactive-development-environment-ide)

## Introduction
The objective of this project was to create an interactive number guessing game, that uses a binary search algorithm to correctly decipher the player's number.

## Features
- A welcome message
- Easy to follow, intuitive play
- The player is asked to specify a range (lower and upper bounds). The range must consist of positive integers, with the bounds having a difference of at least one between them. The program relies on this range to perform binary search logic. 
- Once the lower bound is specified, the program holds on to this number even in the case where the player enters invalid upper bound input
- Extensive error handling for all player inputs throughout
- If invalid input is entered at any time, the player is prompted to try again with infinite tries until valid input is provided
- The player is then asked to enter the number they would like the program to guess. This number must fall within previously specified lower and upper bound limits.
- The program generates a random number for the first guess, this is to offset the otherwise predictable outcome of the binary search algorithm on the first go.
- The player is asked if their chosen number is higher or lower than the guess. The players answer is simultaneously checked according to their chosen number each time to prompt the player to answer again if they have entered incorrect input. 
- The program continues to guess the players number, now using binary search logic for subsequent guesses by finding the midpoint between a progressively diminishing range. The midpoint value is equivelant to each guess made and the final guessed value is the players number.
- Various clear_output() functionality throughout for a clean user interface
- As the program states the player's number, the number of attempts it took to guess this value is shown alongside
- The player is asked if they would like to play again and the game continues until they wish to end the game

## Modules
* Built-in, Random module
* Built-in, clear_output() functionality from IPython.display

## Recommended Interactive Development Environment (IDE)
### **Jupyter notebook**
This program was created and tested using a Jupyter notebook, I recommend running the code in this environment for optimal performance.

### **Version**
The notebook server was run on Python version 3.7.6
