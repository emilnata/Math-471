from . import diff
#from . import intg
#from . import variance

#from Dan Lecocq on stackexchange.com
import struct
def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') 
                   for c in struct.pack('!f', num))
