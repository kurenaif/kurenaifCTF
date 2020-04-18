import hashlib

print("answer: ", end="")
X = int(input())

if "90bb78e59b5fcbddcce29cc40c2b2640" == hashlib.md5((X).to_bytes(16, 'little', signed=False)).hexdigest():
    print("Correct")
else:
    print("Wrong Answer")


