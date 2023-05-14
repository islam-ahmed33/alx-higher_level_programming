#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        mx_n = my_list[0]
        for n in my_list:
            if n > mx_n:
                mx_n = n
        return mx_n
