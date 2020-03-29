from codes import *

def make_alpha(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_alpha = ''
    for letter in word:
        if letter not in new_alpha:
            new_alpha += letter
    for letter in alpha:
        if letter not in new_alpha:
            new_alpha += letter
    return new_alpha

def make_short_alpha(word):
    word = word.replace('j', 'i').replace('x', 'w')
    alpha = 'abcdefghiklmnopqrstuvwyz'
    new_alpha = ''
    for letter in word:
        if letter not in new_alpha:
            new_alpha += letter
    for letter in alpha:
        if letter not in new_alpha:
            new_alpha += letter
    return new_alpha

def dec(ct, key, start_shift):
    ct = ct.lower()
    pt = ''
    alpha = make_short_alpha(key)
    for index, letter in enumerate(ct):
        pt += alpha[(alpha.index(letter) - (index + start_shift)) % 24]
    return pt

def dec_all(ct, key):
    if ' ' in ct:
        ct = ct.split()
    pt = []
    for index, word in enumerate(ct):
        start_shift = index + 1
        pt.append(dec(word, key, start_shift))
    return ' '.join(pt)

def enc_all(pt, key):
    ct = []
    for index, word in enumerate(pt):
        start_shift = index + 1
        ct.append(enc(word, key, start_shift))
    return ' '.join(ct)

def enc(pt, key, start_shift):
    pt = pt.lower()
    ct = ''
    alpha = make_alpha(key)
    for index, letter in enumerate(pt):
        ct += alpha[(alpha.index(letter) + (index + start_shift)) % 26]
    return ct

def try_dec(ct, start_shift, crib = '', words_file = 'all_words'):
    ct = ct.lower()
    with open(words_file + '.txt') as f:
        words = f.read().splitlines()
    with open('all_words.txt') as f:
        english_words = f.read().splitlines()
    for word in words[::100]:
        pt = shifty_decrypt(ct, word, start_shift)
        print(pt)
        '''
        if crib:
            if crib in pt:
                print(word, pt)
        elif pt in english_words:
            print(word, pt)
            '''
