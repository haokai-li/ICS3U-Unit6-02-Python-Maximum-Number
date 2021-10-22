#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculate maximum number
import random


def calculated_maximum_number(calculate_my_numbers):
    # This function calculate maximum number
    loop_number_second = 0
    total_number = 0

    # process
    for loop_number_second in range(0, len(calculate_my_numbers)):
        # output
        print(
            "The random number {0} is {1}".format(
                loop_number_second + 1, calculate_my_numbers[loop_number_second]
            )
        )

        if calculate_my_numbers[loop_number_second] > total_number:
            total_number = calculate_my_numbers[loop_number_second]

    return total_number


def main():
    # This function calculate average
    my_numbers = []
    maximum_number = 0
    loop_number_first = 0

    # process
    for loop_number_first in range(0, 10):
        calculate_number = random.randint(0, 100)
        my_numbers.append(calculate_number)

    # output
    print("Here is a list of random numbers")
    print("")

    # call functions
    maximum_number = calculated_maximum_number(my_numbers)

    # output
    print("")
    print("The largest number is: {0}".format(maximum_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
