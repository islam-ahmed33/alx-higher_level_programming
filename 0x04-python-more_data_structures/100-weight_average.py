#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_W = 0
    total_S = 0
    for s, w in my_list:
        total_S += s * w
        total_W += w

    return total_S / total_W
