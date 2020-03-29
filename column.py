from codes import *

def group(ct, row_len = 0, col_len = 0):
    if row_len:
        return [ct[i : i + row_len] for i in range(0, len(ct), row_len)]
    elif col_len:
        ct_len = len(ct)
        row_len = ct_len // col_len + 1
        split_index = (ct_len % col_len) * row_len
        return group(ct[:split_index], row_len = row_len) + group(ct[split_index:], row_len = row_len - 1)

def rotate(ct_list):
    rotated_list = [[row[i] for row in ct_list][::-1] for i in range(len(ct_list[0]))]
    return [''.join(row) for row in rotated_list]

def transpose(ct_list):
    transposed_list = []
    for i in range(len(ct_list[0])):
        new_row = ''
        for row in ct_list:
            if i < len(row):
                new_row += row[i]
        transposed_list.append(new_row)
    return [''.join(row) for row in transposed_list]

def flatten(ct_list):
    return ''.join(ct_list)

def enc(pt, row_len):
    return flatten(transpose(group(pt, row_len)))

def dec(ct, row_len):
    return flatten(transpose(group(ct, col_len = row_len)))

def try_dec(ct, only_nice = True):
    possibles = []
    length = len(ct)
    for row_length in range(2, length):
        if (not only_nice) or (length % row_length) == 0:
            possibles.append([row_length, col_decrypt(ct, row_length)])
    choice = input("Enter 'o' to examine one at a time or 'a' to print all at once: ")
    print("\nPossible keys:")
    if choice.lower() == 'o':
        for row_length, pt in possibles:
            input('\nEncryption row length %d:\n%s' % (row_length ,pt))
    else:
        for row_length, pt in possibles:
            print('\nEncryption row length %d:\n%s' % (row_length ,pt))
