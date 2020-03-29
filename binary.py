from codes import *

def enc(pt):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ct = []
    for letter in pt:
        ct.append(bin(alpha.index(letter)))
    return ct

def dec(ct_list):
    alpha = 'abcdefghijklmnopqrstuvwxyz' + ' ' * 38
    pt = ''
    for number in ct_list:
        num = int(number, 2)
        print(num)
        pt += alpha[num]
    return pt

def dec_ASCII(ct_list):
    pt = ''
    for number in ct_list:
        num = int(number, 2)
        print(num)
        pt += chr(num)
    return pt

def dec_chain(ct, size = 5):
    if size == 5:
        return dec(column.group(ct, row_len = size))
    elif size == 7:
        return dec_ASCII(column.group(ct, row_len = size))
