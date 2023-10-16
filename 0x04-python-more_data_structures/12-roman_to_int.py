#!/usr/bin/python3
def roman_to_int(roman_string):
    s = roman_string
    d = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}
    res = 0

    for i in range(len(s)):
        if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
            res -= d[s[i]]
        else:
            res += d[s[i]]

    return res
