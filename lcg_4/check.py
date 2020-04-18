import hashlib

print("answer: ", end="")
X = int(input())

if "456223558fd8a5d0f68a5b0642bbc71b" == hashlib.md5((X).to_bytes(16, 'little', signed=False)).hexdigest():
    print("Correct")
else:
    print("Wrong Answer")

