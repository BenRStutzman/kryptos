from codes import *

def dec(ct, key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    pt = ''
    for num in ct:
        if num == 0:
            num = 100
        pt += alpha[(num - key[num // 26]) % 26]
    return pt

def try_dec(ct, crib):
    for i in range(1, 27):
        for j in range(27, 53):
            for k in range(53, 79):
                for l in range(79, 105):
                    pt = mexican.dec(ct, [i, j, k, l])
                    if crib in pt:
                        print(pt)
                        print([i, j, k, l])
