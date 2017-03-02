#!/usr/local/bin/python3

birth = input("please input your birth: ")
birth = int(birth)
if birth < 2000:
    print("00 前")
else:
    print("00 后")