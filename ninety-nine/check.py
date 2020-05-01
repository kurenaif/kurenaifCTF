#!/usr/bin/python3

from Crypto.Util.number import *

print("answer: ", end="")
X = int(input())

cnt = 0
for C in str(X):
    if C == '9':
        cnt += 1

if cnt < 99:
    print("Wrong Answer: Number of \'9\' is less than 99")
    exit(1)

if isPrime(X):
    print("Correct")
else:
    print("Wrong Answer: {} is not prime".format(X))

