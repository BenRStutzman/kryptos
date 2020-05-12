from codes import *

modules = ['tools', 'freq', 'caesar', 'vig', 'column', 'skip', 'hill',
            'ragbaby', 'binary', 'trinary', 'mexican']

def restart():
    #load all the modules again, so functions will be updated
    for module in modules:
        importlib.reload(sys.modules[module])
    print('modules reloaded')

def despace(ct):
    return ''.join(ct.split())

def word_from_order(order):
    with open('all_words.txt', 'r') as f:
        words = f.read().splitlines()
    for pre_word in words:
        word = ''
        for letter in pre_word:
            if letter not in word:
                word += letter
        if len(word) == 6:
            if ord(word[4]) < ord(word[0]) < ord(word[5]) < ord(word[2]) < ord(word[1]) < ord(word[3]):
                print(pre_word)

def read_ct(filename = 'ciphertext.txt', unformat = True):
    filename = str(filename)
    if filename.isdigit():
        filename = 'ciphertext' + filename + '.txt'
    with open(filename) as f:
        ct = f.read()
    if unformat:
        return despace(ct)
    else:
        return ct

def read_pt(filename = 'plaintext.txt', unformat = True):
    filename = str(filename)
    if filename.isdigit():
        filename = 'plaintext' + filename + '.txt'
    return read_ct(filename = filename, unformat = unformat)
