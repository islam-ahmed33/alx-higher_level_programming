#!/usr/bin/python3

def no_c(my_string):
    list_ch = list(my_string)
    new_list_ch = []
    for ch in list_ch:
        if ch != 'c' and ch != 'C':
            new_list_ch.append(ch)
    return "".join(new_list_ch)
