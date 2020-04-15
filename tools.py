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
