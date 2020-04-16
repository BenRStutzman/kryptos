from codes import *

def print_charts(freq_dict, total, alphabetically = False):
    mag = 50 / (max(freq_dict.values()) / total * 100)
    freq_list = [[letter, freq, freq / total * 100] for letter, freq in freq_dict.items() if freq]
    if alphabetically:
        print("\nAlphabetically:\n")
        for letter, freq, perc in sorted(freq_list):
            print('%s: %3d (%2.1f%%) %s' % (letter, freq, perc, '*' * round(perc * mag)))
    else:
        print("\nSorted by Frequency:\n")
        for letter, freq, perc in sorted(freq_list, key = lambda x: x[1], reverse = True):
            print('%s: %4d (%s%2.1f%%) %s' % (letter, freq, ' ' if perc < 10 else '', perc, '*' * round(perc * mag)))

def freq(ct, bi = False, tri = False, alpha_only = True, alphabetically = False):
    ct = ''.join(ct.split())
    if alpha_only:
        for char in set(ct):
            if not char.isalpha():
                ct = ct.replace(char, '')
    print("\nFirst bit of ciphertext:", ct[:50])
    alpha = set(ct).union(set([letter.upper() for letter in ct]))
    freqs = {}
    for letter in alpha:
        monogram = letter.lower()
        freqs[monogram] = freqs.get(monogram, 0) + ct.count(letter)
    print("\nSingle letters:")
    print_charts(freqs, len(ct), alphabetically)

    if bi:
        bigram_freqs = {}
        for letter1, letter2 in itertools.permutations(alpha, 2):
            bigram = (letter1 + letter2).lower()
            bigram_freqs[bigram] = (bigram_freqs.get(bigram, 0)
                + ct.count(letter1 + letter2))
        print("\nBigrams:")
        print_charts(bigram_freqs, len(ct), alphabetically)

    if tri:
        trigram_freqs = {}
        for letter1, letter2, letter3 in itertools.permutations(alpha, 3):
            trigram = (letter1 + letter2 + letter3).lower()
            trigram_freqs[trigram] = (trigram_freqs.get(trigram, 0)
                + ct.count(letter1 + letter2 + letter3))
        print_charts(trigram_freqs, len(ct), alphabetically)
