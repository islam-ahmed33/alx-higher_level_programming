#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    for ch in roman_string:
        for key, val in list(rom.items()):
            if ch == key:
                nums.append(val)
    n = 0
    n_nums = len(nums)
    for i in range(n_nums):
        if i != n_nums - 1:
            x = i + 1
            if nums[i] < nums[x]:
                nums[i] = -nums[i]
        n += nums[i]
    return n
