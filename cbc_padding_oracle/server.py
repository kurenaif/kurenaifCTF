import sys
from typing import List

def bytearray_to_blocks(barray: bytearray) -> List[int]:
    if len(barray) % 16 != 0:
        print("len(barray) % 16 must be 0", file=sys.stderr)

    blocks = [[]]

    for i in range(len(barray)):
        if len(blocks[-1]) == 16 :
            blocks.append([])
        blocks[-1].append(barray[i])
    
    return blocks

def print_blocks(blocks: List[List[int]]):
    for i in range(len(blocks)):
        block = blocks[i]
        print(f"block {i}: ", end="")
        for num in block:
            print(f"|{num:x}", end="")
        print("|")
    
print_blocks(bytearray_to_blocks(bytearray(b"0123456789abcdef0123456789abcdef")))
