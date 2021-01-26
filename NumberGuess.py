"""Binary Search Number Guessing Game"""
from IPython.display import clear_output
import random


def welcome():
    """Prints a welcome message."""
    
    print("Welcome to this number guessing game!\nEnter range values, think of a number and we'll guess it for you.\n")
    
def lower_bound():
    """Player defines the lower bound value of the range."""
    
    while True:
        try:
            lower = int(input("Please enter positive integers for range values.\n\nEnter your lower bound: "))
            if lower <= 0:
                clear_output()
                print("Lower bound must be greater than 0!")
                continue
        except:
            clear_output()
            print("Invalid input! Try again.")
        else:
            clear_output()
            break
    return lower

def upper_bound():
    """Player defines the upper bound value of the range."""
    
    while True:
        try:
            upper = int(input(f"Your lower bound is: {lower}\nEnter your upper bound: "))
            if upper <= 0:
                clear_output()
                print("Upper bound must be greater than 0!")
                continue
        except:
            clear_output()
            print("Invalid input! Try again.")
        else:
            break
    return upper

def users_integer(lower, upper):
    """Player defines an integer for the program to guess."""
    
    while True:
        try:
            users_number = int(input(f"Your specified range is between {lower} and {upper}.\nPlease enter the positive integer you would like us to guess: "))
            if users_number <= 0:
                    clear_output()
                    print("Number must be greater than 0!")
                    continue
        except:
            clear_output()
            print("Invalid input! Try again.")
        else:
            if users_number in range(lower, upper):
                return users_number
                break
            else:
                clear_output()
                print(f"The number you choose must fall within the bounds you specified!\n Choose a number between {lower} and {upper}.")

def guess(a, b):
    """Generates a random integer for the first guess and uses binary search logic for subsequent guesses."""
    
    global lower_range
    global upper_range

    if len(guess_list) == 0:
        guess = random.randint(a, b)
        lower_range = a
        upper_range = b
    else:
        if answer == "L":
            upper_range = guess_list[-1]
            guess = (lower_range + upper_range) // 2

        else:
            lower_range = guess_list[-1]
            guess = (lower_range + upper_range) // 2

    guess_list.append(guess)
    
def higher_lower():
    """Asks the player if the guess was higher or lower than their number."""
    
    global answer
    acceptable_values = ["H", "L"]
    
    while True:
        answer = input(f"Our guess was {guess_list[-1]}!\n\nIs your number higher or lower than {guess_list[-1]}?\nType 'h' for higher or 'l' for lower. ").upper()
        
        if answer not in acceptable_values:
            clear_output()
            print("Invalid input! Enter 'h' or 'l'.")
            
        elif player_choice > guess_list[-1] and answer == "H":
            break
            
        elif player_choice < guess_list[-1] and answer == "L":
            break
            
        else:
            clear_output()
            print("Check your input is correct! Try again.")           

def replay():
    """Asks the player if they would like to continue playing."""
    
    ask = True
    acceptable_values = ["yes", "no"]
    while ask:
        choice = input("Would you like to play agin?\nEnter 'yes' or 'no':").lower()
        
        if choice not in acceptable_values:
            clear_output()
            print("Type 'Yes' or 'No'.")
        else:
            break
            
    if choice == "yes":
        clear_output()
        return True
    else:
        clear_output()
        print("\nThank you for playing!")
        return False


game_on = True
guessing = True
guess_list = []

welcome()
while game_on:
    lower = lower_bound()
    while True:
        upper = upper_bound()
        if lower > upper:
            clear_output()
            print("Lower bound value must be less than upper bound!")
        elif upper - lower == 1:
            clear_output()
            print("The difference between upper and lower bounds must be greater than 1.")
        elif upper == lower:
            clear_output()
            print("You must choose different numbers for upper and lower bounds.")
        else:
            clear_output()
            print(f"The range we will use to guess your number is between {lower} and {upper}.")
            break
            
    player_choice = users_integer(lower, upper)

    while guessing:
        clear_output()
        guess(lower, upper)
        if guess_list[-1] == player_choice:
            print(f"Your number is {guess_list[-1]}! \nThis is how many guesses it took: {len(guess_list)}")
            guessing = False
            break
        else:
            higher_lower()

    if replay():
        guessing = True
        continue
    else:
        game_on = False
