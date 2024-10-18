#!/usr/bin/python3

import sys

def rot(text,num):
    result = []
    for char in text:
        
        if 'a' <= char <= 'z':
            
            result.append(chr((ord(char) - ord('a') + int(num)) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            
            result.append(chr((ord(char) - ord('A') + int(num)) % 26 + ord('A')))
        else:
            
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <text> <rot_num>")
        sys.exit(1)

    input_text = sys.argv[1]
    input_num  = sys.argv[2]
    rot_output = rot(input_text, input_num)
    print(f"ROT{input_num} Output: {rot_output}")

