#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) == dict:
        for n in sorted(a_dictionary):
            print(f"{n}: {a_dictionary[n]}")
