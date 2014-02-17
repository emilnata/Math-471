from __future__ import print_function
from . import diff
#from . import intg
#from . import variance

#from Dan Lecocq on stackexchange.com
def binary(num):
        import struct
        s = ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') 
                    for c in struct.pack('!d', num))
        print(s,':')
        print('            num = ', num)
        print('       sign bit = ', s[0])
        print('  exponent bits = ', s[1:12])
        print(' exponent value = ', int(s[1:12], 2))
        print(' precision bits = ', s[12:],'\n')

