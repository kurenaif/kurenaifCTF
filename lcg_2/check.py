import hashlib

print("answer: ", end="")
X = int(input())

if "f9c62a57ddf7db81094c62c6ac01f72a" == hashlib.md5((X).to_bytes(16, 'little', signed=False)).hexdigest():
    print("Correct")
else:
    print("Wrong Answer")