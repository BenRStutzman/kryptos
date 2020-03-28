from codes import *

def shift(letter, number):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return alpha[(alpha.index(letter.lower()) + number) % 26]

def enc(ct, number):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    pt = ''
    for letter in ct:
        if letter.lower() in alpha:
            pt += shift(letter, number)
        else:
            pt += letter
    return pt

def dec(ct, number):
    return csr_encrypt(ct, -number)

def try_dec(ct, decode = True):
    for number in range(26):
        print("\nencoding shift:", number)
        print(caesar(ct, number, decode))
