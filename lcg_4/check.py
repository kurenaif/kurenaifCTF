import hashlib

print("answer: ", end="")
X = int(input())

if "3b2e252b2e51143dfb4d03dda4361139" == hashlib.md5((X).to_bytes(16, 'little', signed=False)).hexdigest():
    print("Correct")
else:
    print("Wrong Answer")
