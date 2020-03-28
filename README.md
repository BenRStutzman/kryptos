# kryptos
Tools for codebreaking, designed for the Kryptos codebreaking competition hosted by CWU.

First, make sure you have numpy installed (used for matrix stuff for the Hill cipher).

Then, start Python in your command line, and run

from codes import *

And then you're good to go with lots of tools like
  caesar.shift('h', 1)
  vig.try_dec('FSF QWNYCPR VYE EVPW GTUPRPCS JMASSY!', crib = 'cipher')
  column.group('Put this into rows of three, please', row_len = 3)
  
and many others.
