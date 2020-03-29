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
    return enc(ct, -number)

def try_dec(ct):
    for number in range(26):
        print("\nencoding shift:", number)
        print(dec(ct, number))

def try_dec_list(ct):
    answers = []
    for number in range(26):
        answers.append(dec(ct, number))
    return answers
