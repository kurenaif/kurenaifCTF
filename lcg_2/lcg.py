import os
import math
import binascii

class MyLCG:
    def __init__(self, S):
        self.A = int(binascii.hexlify(os.urandom(16)), 16)
        self.B = int(binascii.hexlify(os.urandom(16)), 16)
        self.M = int(binascii.hexlify(os.urandom(16)), 16)
        self.x = (S % self.M)
    def next(self):
        self.x = ((self.A * self.x) + self.B) % self.M
        return self.x

r = MyLCG(int(binascii.hexlify(os.urandom(16)), 16))
print("A = " + str(r.A))
# print("B = " + str(r.B))
print("M = " + str(r.M))

cnt = 2
for i in range(cnt):
    print("X[{}] = {}".format(i,r.next()))

print("X[{}] = ?".format(cnt))
print("X[{}] = {}".format(cnt, r.next()))