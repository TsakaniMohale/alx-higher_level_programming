#!/usr/bin/python3
def remove_charat(str, n):
    s = ""
    for i in range(len(str)):
        if i != n:
            s = s + str[i]
    return (s)
