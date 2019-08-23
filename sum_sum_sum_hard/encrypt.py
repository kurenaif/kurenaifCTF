#!/usr/loca/bin python3
import typing
from fractions import Fraction
import random
import numpy as np
from flag import flag

# get primes in [0,num)
def prime_list(num):
    a = [True for i in range(num)]

    a[0] = False
    a[1] = False

    res = []

    for i in range(2,num):
        if a[i]:
            res.append(i)
        a[i] = False
        for j in range(i,num,i):
            a[j] = False
    
    return res
    
def string_to_ord_list(S):
    cs = []
    for c in S:
        cs.append(ord(c))
    return cs

def encrypt(cs, num):
    temp = cs + cs
    res = []
    for i in range(len(cs)):
        res.append(sum(temp[i:i+num]))
    
    return res

m = flag # note: len(m) is prime number!
m = string_to_ord_list(m)
print("sum = ", sum(m))
primes =  prime_list(len(m))
print("primes = ", primes)
for i in range(128):
    m = encrypt(m, random.choice(primes))
C = m

print("C = ", C)