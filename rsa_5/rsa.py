from Crypto.Util.number import *
from Crypto.Random import *
import secret
import math

p = getRandomNBitInteger(512)
while not isPrime(p):
    p = getRandomNBitInteger(512)

q = getRandomNBitInteger(512)
while not isPrime(q):
    q = getRandomNBitInteger(512)

n = p * q
m = bytes_to_long(secret.flag.encode('utf-8')) # ここにフラグを数値に変換したものが入ります

phi = (p-1)*(q-1)

e = getRandomNBitInteger(64)
while math.gcd(phi, e) != 1:
    e = getRandomNBitInteger(64)

d = inverse(e, phi)

print("d = {}".format(d))
print("n = {}".format(n))
print("c = {}".format(pow(m,d,n)))
