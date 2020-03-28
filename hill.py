from codes import *

# Solve linear equation with your calculator (rref the matrix), but need integers
# Find modular inverse matrix at https://planetcalc.com/3324/

def enc(pt, matrix):
    pt = despace(pt.lower())
    pt += (len(pt) % 3) * 'x'
    pt = [ord(letter) - 97 for letter in pt]
    matrix = numpy.array(matrix)
    ct = ''
    i = 0
    while i < len(pt):
        pt_chunk = numpy.matrix.transpose(numpy.matrix(pt[i:i + 3]))
        ct_chunk = matrix.dot(pt_chunk)
        ct += ''.join([chr(int(ct_chunk[i] % 26) + 97) for i in range(3)])
        i += 3
    return ct

def dec(pt, matrix):
    return hill_encrypt(pt, matrix)
