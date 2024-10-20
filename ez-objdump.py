#!/usr/bin/python3

import os
import sys

def init():

    if len(sys.argv) != 3:
        print("[!] require argument <filename> <symbolname>")
        sys.exit()

    #return sys.argv

    elif sys.argv[2] == "-l":
        print("list")
        
        cmd = "objdump -M intel -d "+sys.argv[1]+" | grep -E \"<.*?>:\""

        os.system(cmd)
        sys.exit()
    
    return sys.argv

def main():

    args = init()

    cmd_fmt = f"objdump -M intel -d {args[1]} | awk \'/<{args[2]}>:/,/^$/\'"
    #print(cmd_fmt)
    os.system(cmd_fmt)

if __name__ == "__main__":

    main()

