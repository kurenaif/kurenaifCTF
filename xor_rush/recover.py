import sys

def recover(s):
    swap_list = [(15, 0), (17, 1), (8, 2), (16, 3), (10, 4), (13, 5), (9, 6), (14, 7), (5, 8), (12, 9), (3, 10), (7, 11), (19, 12), (6, 13), (0, 14), (4, 15), (2, 16), (18, 17), (1, 18), (11, 19), (20, 20)]
    m = list(s)
    m.sort()
    if len(swap_list) != len(s):
        print("string length must be " + str(len(swap_list)))
        return ""
    res = ["?" for i in range(len(m))]
    for s in swap_list:
        l = s[0]
        r = s[1]
        res[l] = m[r]
    return "".join(res)

print(recover(sys.argv[1]))