from Crypto.Util.number import *
from Crypto.Random import *
import secret

p = getRandomNBitInteger(64)
while not isPrime(p):
    p = getRandomNBitInteger(64)

q = getRandomNBitInteger(512)
while not isPrime(q):
    q = getRandomNBitInteger(512)

n = p * q
e = 65537

m = bytes_to_long(secret.flag.encode('utf-8')) # ここにフラグを数値に変換したものが入ります

print("n = {}".format(n))
print("e = {}".format(e))
print("c = {}".format(pow(m,e,n)))
