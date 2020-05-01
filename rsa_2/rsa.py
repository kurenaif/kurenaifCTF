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

n1 = p * q
n2 = q * r
e = 65537
m1 = bytes_to_long(secret.flag.encode('utf-8')) # ここにフラグを数値に変換したものが入ります
m2 = bytes_to_long("this is dummy message".encode('utf-8') )

print("e = {}".format(e))
print("n1 = {}".format(n1))
print("c1 = {}".format(pow(m1,e,n1)))
print("n2 = {}".format(n2))
print("c2 = {}".format(pow(m2,e,n2)))
