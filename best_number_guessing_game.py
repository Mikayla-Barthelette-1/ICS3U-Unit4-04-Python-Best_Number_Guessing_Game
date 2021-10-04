#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program creates the best number guessing game

import random


def main():
    # this function creates the game

    # input & process & output
    random_number = random.randint(0, 9)  # a number between 0 and 9

    while True:
        user_input = input("Enter a number between 0 - 9: ")
        try:
            number_guessed = int(user_input)
            if number_guessed == random_number:
                print("Correct! The number was {0}.".format(random_number))
                print("\nDone.")
                break
            elif number_guessed > random_number:
                print("{0} is too high.".format(number_guessed))
            else:
                print("{0} is too low.".format(number_guessed))
        except Exception:
            print("Invalid input.")
        finally:
            print("")


if __name__ == "__main__":
    main()
