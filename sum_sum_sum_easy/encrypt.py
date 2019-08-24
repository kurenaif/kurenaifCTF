#!/usr/loca/bin python3
import typing
from fractions import Fraction
import random
from flag import flag
import os

def encrypt(S, num):
    cs = []
    for c in S:
        cs.append(ord(c))
    
    cs += cs
    res = []
    for i in range(len(S)):
        res.append(sum(cs[i:i+num]))
    return res

def check(m):
    for i in range(2,len(m)):
        if len(m) % i == 0:
            return False
    return True

m = flag # note: len(m) is prime number!
if not check(m):
    print("len(m) must be prime number!")
    os.Exit(1)
c = encrypt(m, random.randrange(len(m)-1)+1)
print("C =", c)
