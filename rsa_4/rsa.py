from Crypto.Util.number import *
from Crypto.Random import *
import secret

p = getRandomNBitInteger(512)
while not isPrime(p):
    p = getRandomNBitInteger(512)

q = getRandomNBitInteger(512)
while not isPrime(q):
    q = getRandomNBitInteger(512)

r = getRandomNBitInteger(512)
while not isPrime(r):
    r = getRandomNBitInteger(512)

n = p * q * r
m = bytes_to_long(secret.flag.encode('utf-8')) # ここにフラグを数値に変換したものが入ります
e = 65537

print("e = {}".format(e))
print("n = {}".format(n))
print("p = {}".format(p))
print("q = {}".format(q))
print("r = {}".format(r))
print("c = {}".format(pow(m,e,n)))
