#!/usr/bin/python3

def no_c(my_string):
    list_ch = list(my_string)
    for ch in list_ch:
        if ch == 'c' or ch == 'C':
            list_ch.remove(ch)
    return("".join(list_ch))
