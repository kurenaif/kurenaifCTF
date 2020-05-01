import hashlib

print("answer: ", end="")
X = int(input())

if "23f30835b3d7dbabeb32d3f06e5fb063" == hashlib.md5((X).to_bytes(16, 'little', signed=False)).hexdigest():
    print("Correct")
else:
    print("Wrong Answer")
