from Crypto.Util.number import *
from Crypto.Random import *
import secret

p = getRandomNBitInteger(512)
while not isPrime(p):
    p = getRandomNBitInteger(512)

q = getRandomNBitInteger(512)
while not isPrime(q):
    q = getRandomNBitInteger(512)

n = p * q
m = bytes_to_long(secret.flag.encode('utf-8')) # ここにフラグを数値に変換したものが入ります
e = 3

print("e = {}".format(e))
print("n = {}".format(n))
print("c = {}".format(pow(m,e,n)))
