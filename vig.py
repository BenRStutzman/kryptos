from codes import *

def all_rotations(word):
    rotations = []
    for i in range(len(word)):
        rotations.append(word[i:] + word[:i])
    return rotations

def enc(pt, key, tableau = 'standard'):
    with open('tableaus/' + tableau + '.txt') as f:
        tableau = f.read().splitlines()
    key = key.upper()
    key_len = len(key)
    first_col = [row[0] for row in tableau][1:]
    first_row = tableau[0][1:]
    tableau = [row[1:] for row in tableau[1:]]
    ct = ''
    key_pos = 0
    for letter in pt:
        if letter.isalpha():
            row = first_col.index(key[key_pos % key_len])
            col = first_row.index(letter.upper())
            ct += tableau[row][col]
            key_pos += 1
        else:
            ct += letter
    return ct

def get_tableau(tableau):
    tableau_file = 'tableaus/' + tableau + '.txt'
    if not os.path.exists(tableau_file):
        make_tableau(tableau, filename = tableau)
    with open(tableau_file) as f:
        return f.read().splitlines()

def dec(ct, key = '', tableau = 'standard',
                real_key = '', key_len = 0, first_col = [], real_tableau = [],
                first_row = ''):
    if real_tableau:
        tableau = real_tableau
        key = real_key
    else:
        if not key:
            print("No key or real_key included...")
            raise Exception
        tableau = get_tableau(tableau)
        key = key.upper()
        key_len = len(key)
        first_col = [row[0] for row in tableau][1:]
        first_row = tableau[0][1:]
        tableau = [row[1:] for row in tableau[1:]]
    pt = ''
    key_pos = 0
    for letter in ct:
        if letter.isalpha():
            row = first_col.index(key[key_pos % key_len])
            col = tableau[row].index(letter.upper())
            pt += first_row[col]
            key_pos += 1
        else:
            pt += letter
    return pt

def pt_and_key(pt, key):
    return str.format('%s\n(key: %s)\n' % (pt, key))

def try_dec(ct, key_len = 0, crib = '', words = [],
    thresholds = {'E': 0.07, 'T': 0.05, 'A': 0.03}, tableau = 'standard',
    rotations = False):
    tableau = get_tableau(tableau)
    first_col = [row[0] for row in tableau][1:]
    first_row = tableau[0][1:]
    tableau = [row[1:] for row in tableau[1:]]
    possibles = {}
    num_alpha = 0
    for letter in ct:
        if letter.isalpha():
            num_alpha += 1
    crib = crib.upper()
    if not words:
        with open('all_words.txt') as f:
            words = f.read().splitlines()
    for key in words:
        key_length = len(key)
        if (not key_len) or (key_length == key_len):
            pt = dec(ct, real_key = key.upper(), real_tableau = tableau,
                key_len = key_length, first_col = first_col, first_row = first_row)
            if crib:
                if crib in pt:
                    possibles[key] = pt
            else:
                for letter, min in thresholds.items():
                    if pt.count(letter) / num_alpha < min:
                        break
                else:
                    possibles[key] = pt
    print("\nFound %d possible key%s." % (len(possibles), 's' if len(possibles) != 1 else ''))
    if len(possibles) == 1:
        key, pt = list(possibles.items())[0]
        print(pt_and_key(pt, key))
    elif len(possibles) > 1:
        choice = input("Enter 'o' to examine one at a time or 'a' to print all at once: ")
        if choice.lower() == 'o':
            print("\nPossible decryptions:\n")
            for key, pt in possibles.items():
                input(pt_and_key(pt, key))
        else:
            print("\nPossible decryptions:\n")
            for key, pt in possibles.items():
                print(pt_and_key(pt, key))

def strange_key(ct, crib, tableau = 'standard'):
    ct = ''.join(ct.split())
    tableau = get_tableau(tableau)
    crib = crib.upper()
    crib_len = len(crib)
    first_col = [row[0] for row in tableau][1:]
    first_row = tableau[0][1:]
    tableau = [row[1:] for row in tableau[1:]]
    keys = []

    for i in range(len(ct) - crib_len + 1):
        section = ct[i:i + crib_len]
        key = ''

        crib_pos = 0
        for letter in section:
            if letter.isalpha():
                col = first_row.index(crib[crib_pos % crib_len])
                cur_col = [row[col] for row in tableau]
                row = cur_col.index(letter.upper())
                key += first_col[row]
                crib_pos += 1
            else:
                key += letter
        keys.append(key)

    if len(keys) == 1:
        print('key:', keys[0])
        return

    choice = input("Enter 'o' to examine one at a time or 'a' to print all at once: ")
    if choice.lower() == 'o':
        print("\nPossible keys:")
        for pos, key in enumerate(keys):
            input('\nPosition %d:\n%s' % (pos + 1, key))
    else:
        print("\nPossible keys:")
        for pos, key in enumerate(keys):
            print('\nPosition %d:\n%s' % (pos + 1, key))

def crib_and_pos(ct, pos, crib, tableau = 'standard'):
    seg = ct[pos - 1 : pos - 1 + len(crib)]
    strange_key(seg, crib = crib, tableau = tableau)

def make_tableau(keyword, filename = 'new_tableau', match_grid = True):
    first_line = ''
    for letter in keyword.upper():
        if letter not in first_line:
            first_line += letter
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if letter not in first_line:
            first_line += letter
    lines = []

    for i in range(26):
        lines.append(first_line)
        first_line = first_line[1:] + first_line[0]

    if match_grid:
        side_key = ''.join([line[0] for line in lines])
        top_key = lines[0]
    else:
        side_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        top_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for index, letter in enumerate(side_key): #insert side key
        lines[index] = letter + lines[index]

    lines.insert(0, ' ' + top_key) #insert top key

    with open('tableaus/' + filename + '.txt', 'w') as f:
        for line in lines:
            f.write(line + '\n')

def IC(ct, interval = 0):
    for char in ct:
        if not char.isalpha():
            ct = ct.replace(char, '')
    if interval:
        ICs = []
        for i in range(interval):
            ICs.append(IC(ct[i::interval]))
        return sum(ICs) / len(ICs)
    num_sum = 0
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        cnt = ct.count(letter) + ct.count(letter.lower())
        num_sum += (cnt * (cnt - 1))
    try:
        index = num_sum / (len(ct) * (len(ct) - 1))
    except ZeroDivisionError:
        index = 0
    return index

def try_ICs(ct, sort = True, max_int = 30):
    ICs = []
    for interval in range(1, max_int + 1):
        index = IC(ct, interval)
        ICs.append([interval, index])
    if sort:
        ICs = sorted(ICs, key = lambda x: x[1], reverse = True)
    for interval, index in ICs:
        print("Interval: %d\tI.C.: %f" % (interval, index))

#print(decrypt(ct, 'ambroisethomas'))
