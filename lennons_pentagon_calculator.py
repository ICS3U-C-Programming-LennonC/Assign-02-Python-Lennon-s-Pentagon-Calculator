#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: October 11th, 2026
# This program calculates the area and perimeter of a pentagon from just one side length.
#
import math


def main():
    # Greet the user, then get the side length from the user, and convert it to a float.
    length = float(input("Welcome to Lennon’s Pentagon Calculator. Please enter the side length of your pentagon (cm): "))

    # Calculate the area and perimeter of the pentagon.
    area = (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (length**2)

    perimeter = 5 * length

    # Display the area and perimeter to the user with the proper units.
    print("The area of the pentagon is: {:.2f}cm²".format(area))
    print("The perimeter of the pentagon is: {}cm".format(perimeter))


if __name__ == "__main__":
    main()
