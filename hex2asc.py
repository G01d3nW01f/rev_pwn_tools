#!/usr/bin/python3

import sys

def hex_to_ascii(hex_str):
    
    ascii_chars = [chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)]
    return ''.join(ascii_chars)

if __name__ == "__main__":
    

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <hex_value>")
        sys.exit(1)
    
    
    hex_input = sys.argv[1]

    
    if hex_input.startswith("0x"):
        hex_input = hex_input[2:]
    
    ascii_output = hex_to_ascii(hex_input)
    print(f"ASCII Output: {ascii_output}")

