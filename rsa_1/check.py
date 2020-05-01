from Crypto.Util.number import *

print("answer: ", end="")
X = int(input())
print(long_to_bytes(X).decode('utf-8'))
