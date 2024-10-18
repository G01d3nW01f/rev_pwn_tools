#!/usr/bin/python3

import sys

def init():
    
    if len(sys.argv) != 2:
        print("[!]Require argument <dec num>")
        sys.exit()

    return sys.argv[1]

def main():

    dec_num = init()

    try:
        print(hex(int(dec_num)))
    except:
        print("[!]Invalid input")


if __name__ == "__main__":

    main()
