import os
import math
import binascii
import random

# ref: https://qiita.com/srtk86/items/609737d50c9ef5f5dc59
def is_prime(n):
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for _ in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True

class MyLCG:
    def __init__(self, S):
        self.A = int(binascii.hexlify(os.urandom(16)), 16)
        self.B = int(binascii.hexlify(os.urandom(16)), 16)
        
        while True:
            self.M = int(binascii.hexlify(os.urandom(16)), 16)
            if is_prime(self.M):
                break

        self.x = (S % self.M)
    def next(self):
        self.x = ((self.A * self.x) + self.B) % self.M
        return self.x

r = MyLCG(int(binascii.hexlify(os.urandom(16)), 16))
# print("A = " + str(r.A))
# print("B = " + str(r.B))
print("# M is prime number!")
print("M = " + str(r.M))

cnt = 3
for i in range(cnt):
    print("X[{}] = {}".format(i,r.next()))

print("X[{}] = ?".format(cnt))
print("X[{}] = {}".format(cnt, r.next()))