import hashlib
from flag import flag

print("length:", len(flag))
assert flag[0:12] == "kurenaifCTF{"
m = list(flag)
m.sort()

res = 0
memo = set()
for c in m:
    assert 33 <= ord(c) < 127
    assert c not in memo
    memo.add(c)
    res ^= int(hashlib.md5(c.encode("utf-8")).hexdigest(), 16)

print(res)