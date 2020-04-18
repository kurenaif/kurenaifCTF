import hashlib

print("answer: ", end="")
X = int(input())

if "3a4ebd5c90d724471ed49538de4eb417" == hashlib.md5((X).to_bytes(16, 'little', signed=False)).hexdigest():
    print("Correct")
else:
    print("Wrong Answer")
