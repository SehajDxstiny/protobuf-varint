'''
1. convert to number, then convert to binary - done 
2. split the binary into 7 bits each from lsb - done 
3. add msb (continution bits) - done 
4. concatenate and convert to hexadecimal - done 
'''
 
'''not spending time to refactor, this is just the first implementation, could be alot of improvements, especially in the split_into_groups function. and overall the most efficient way is to use bitwise operations'''

import struct
from itertools import zip_longest

with open('150.uint64', 'rb') as file:
    integer = struct.unpack('>Q', file.read())[0]

binary = bin(integer)[2:]
print("binary:", binary)

def split_into_groups(iterable, group_size, fill_value=None):
    it = iter(iterable)
    groups = zip_longest(*[it] * group_size, fillvalue=fill_value)
    reversed_groups = [list(group)[::-1] for group in groups]
    return reversed_groups

groups = split_into_groups(binary[::-1], 7, fill_value='0')

with_cont = [["0"] + list(byte) if idx == (len(groups) - 1) else ["1"] + list(byte) for idx, byte in enumerate(groups)]

concat_bytes= "".join("".join(inner_array) for inner_array in with_cont)

final = hex(int(''.join(with_cont), 2))
print(final)
