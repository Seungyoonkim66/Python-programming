import binascii
import sys

def trans(a):
    if a == "0":
        a = "0000"
    if a == "1":
        a = "0001"
    if a == "2":
        a = "0010"
    if a == "3":
        a = "0011"
    if a == "4":
        a = "0100"
    if a == "5":
        a = "0101"
    if a == "6":
        a = "0110"
    if a == "7":
        a = "0111"
    if a == "8":
        a = "1000"
    if a == "9":
        a = "1001"
    if a == "a":
        a = "1010"
    if a == "b":
        a = "1011"
    if a == "c":
        a = "1100"
    if a == "d":
        a = "1101"
    if a == "e":
        a = "1110"
    if a == "f":
        a = "1111"

    return a

def Rtype(i):
    funct = i[26:]
    rs = int(i[6:11], 2)
    rt = int(i[11:16], 2)
    rd = int(i[16:21], 2)
"mips_sim.py" 216L, 6076C                             1,1           Top
