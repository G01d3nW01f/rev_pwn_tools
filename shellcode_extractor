#!/usr/bin/python3

from capstone import *
from pwn import *
import sys


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def red():
    print(bcolors.RED)

def endc():
    print(bcolors.ENDC)




if len(sys.argv) != 3:
    print("[!]require argument <filename> <section_name>")
    print(f"[+]usage: {sys.argv[0]} file .text")
    sys.exit()



file_name = sys.argv[1]
sect_name = sys.argv[2]

file = ELF(f"{file_name}")
shellcode = file.section(f"{sect_name}")

print("========================================================================")
print(''.join(f'\033[93m\\x{byte:02x}\033[0m' for byte in shellcode))
print("========================================================================")

code = shellcode
md = Cs(CS_ARCH_X86, CS_MODE_64)

print("========================================================================")
for i in md.disasm(code, 0x1000):
    hex_bytes = ' '.join(f'{b:02x}' for b in i.bytes)
    print(f"\033[37m{hex_bytes:<20}\t\033[93m{i.mnemonic}\t{i.op_str}\033[0m")
print("========================================================================")
