#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ simple delet the value of adictionary with its keys"""
    if key in a_dictionary:
        del (a_dictionary[key])
    return a_dictionary
