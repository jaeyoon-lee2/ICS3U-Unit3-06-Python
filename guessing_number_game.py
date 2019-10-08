#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program guesses random numbers


import random


def main():
    # this function guesses random numbers

    # input
    integer_as_string = input("Enter the number(1 ~ 10): ")

    # process
    try:
        some_variable = random.randint(1, 10+1)  # a number between 1 and 10
        integer_as_number = int(integer_as_string)
        if some_variable == integer_as_number:
            # output
            print("It is correct!")
        else:
            print("It is wrong")
            print("The number is {}".format(some_variable))
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
