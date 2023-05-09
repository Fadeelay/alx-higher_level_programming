#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod_number = abs(number) % 10
if (number < 0):
    mod_number= -mod_number
if (mod_number > 5):
    print("Last digit of {} is {} and is greater than 5".format(number,mod_number))
elif (mod_number == 0):
    print("Last digit of {} is {] and is 0".format(number,mod_number))
elif (mod_number > 0 and mod_number < 6):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,mod_number))
