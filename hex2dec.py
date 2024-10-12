#!/usr/bin/python3

import sys



def init():
    
    if len(sys.argv) != 2:
        print("require argument for convert hex number")
        sys.exit()

    hex_str = str(sys.argv[1])
    return hex_str



def calc(hex_str):

    print(int(hex_str, 16))



def main():

    hex_str = init()
    calc(hex_str)


main()

