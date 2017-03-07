#!/usr/local/bin/python3

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operad type')

    if (x >= 0):
        return x
    else:
        return -x

def nop():
    pass

