from codes import *

# Iterative Python 3 program to find
# modular inverse using extended
# Euclid algorithm

# This code is contributed by Nikita tiwari.

# Returns modulo inverse of a with
# respect to m using extended Euclid
# Algorithm Assumption: a and m are
# coprimes, i.e., gcd(a, m) = 1
def new_skip_size(skip_size, text_len) :
    a = skip_size
    m = text_len
    m0 = m
    y = 0
    x = 1

    if (m == 1) :
        return 0

    while (a > 1) :

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0) :
        x = x + m0
    return x

def enc(pt, skip_size):
    text_len = len(pt)
    ct = ''
    for i in range(1, text_len + 1):
        ct += pt[(skip_size * i - 1) % text_len]
    return ct

def dec(ct, skip_size):
    text_len = len(ct)
    pt = ''
    try:
        new_skip = new_skip_size(skip_size, text_len)
    except ZeroDivisionError:
        return 0
    #print("decryption skip size:", new_skip)
    return ecn(ct, new_skip)

def skip_and_key(pt, skip_size):
    return str.format('%s\n(skip size: %d)\n' % (pt, skip_size))

def try_dec(ct):
    possibles = {}
    for skip_size in range(1, len(ct) + 1):
        pt = dec(ct, skip_size)
        if pt:
            possibles[skip_size] = pt
    choice = input("Enter 'o' to examine one at a time or 'a' to print all at once: ")
    if choice.lower() == 'o':
        print("\nPossible decryptions:\n")
        for key, pt in possibles.items():
            input(skip_and_key(pt, key))
    else:
        print("\nPossible decryptions:\n")
        for key, pt in possibles.items():
            print(skip_and_key(pt, key))
