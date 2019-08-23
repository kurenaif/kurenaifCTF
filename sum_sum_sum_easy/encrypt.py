#!/usr/loca/bin python3
import typing
from fractions import Fraction
import random
from flag import flag

def encrypt(S, num):
    cs = []
    for c in S:
        cs.append(ord(c))
    
    cs += cs
    res = []
    for i in range(len(S)):
        res.append(sum(cs[i:i+num]))
    return res

m = flag # note: len(m) is prime number!
c = encrypt(m, random.randrange(len(m)-1)+1)
for i in range(len(c)):
    print("C[{}]={}".format(i,c[i]))