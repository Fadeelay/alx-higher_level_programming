#!/usr/bin/python3
def no_c(my_string):
    """Remove all occurence of c inmy string"""
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]
    return new_string
