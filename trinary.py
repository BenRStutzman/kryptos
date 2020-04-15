from codes import *

def tri_to_letter(trinary):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return alpha[int(trinary, 3) - 1]

def dec(ct_list):
    pts = []
    for mutation in [
        {'0': '0', '1': '1', '2': '2'},
        {'0': '1', '1': '0', '2': '2'},
        {'0': '2', '1': '1', '2': '0'},
        {'0': '0', '1': '2', '2': '1'},
        {'0': '1', '1': '2', '2': '0'},
        {'0': '2', '1': '0', '2': '1'},
    ]:
        pt = ''
        for trinary in ct_list:
            pt += tri_to_letter(mutate(trinary, mutation))
        pts.append(pt)
    return pts


def mutate(trinary, mutation):
    new_trinary = ''
    for digit in trinary:
        new_trinary += mutation[digit]
    return new_trinary
