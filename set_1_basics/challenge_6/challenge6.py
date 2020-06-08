#!/usr/bin/env python3
from binascii import hexlify
import base64
import math

def hamming_distance(str1, str2):
    """
    For binary strings a and b the Hamming distance is equal to the number of ones (population count) in a XOR b.
    """
    diffs = [a^b for a, b in zip(str1, str2)]
    count = 0
    for diff in diffs:
        while diff != 0:
           diff = diff & (diff -1)
           count += 1
    return count

def find_keysize(msg):
    sizes = []
    for size in range(2, 41):
        blocks = seperate(msg, size)
        dists = []
        for b1, b2 in zip(blocks[0::2], blocks[1::2]):
            dist = hamming_distance(b1, b2)
            dists.append(dist/size)
        sizes.append(((sum(dists)/len(dists))/38, size))
    return sizes   

def seperate(msg, blocksize):
    blockcount = math.ceil(len(msg)/blocksize)
    blocks = []
    for i in range(blockcount):
        blocks.append(msg[i*blocksize: i*blocksize+blocksize]) 
    return blocks

def transpose(blocks):
    size = len(blocks[0])
    transposed = [bytearray() for i in range(size)]
    for block in blocks:
        for i, b in enumerate(block):
            transposed[i].append(b)
    return transposed

def repeating_key_xor(msg, key):
    klen = len(key)
    return bytes([c ^ key[i % klen] for i, c in enumerate(msg)])

LETTER_DISTRIBUTION = {
        'a': 8.497,
        'b': 1.492,
        'c': 2.202,
        'd': 4.253,
        'e': 11.162,
        'f': 2.228,
        'g': 2.015,
        'h': 6.094,
        'i': 7.546,
        'j': 0.153,
        'k': 1.292,
        'l': 4.025,
        'm': 2.406,
        'n': 6.749,
        'o': 7.507,
        'p': 1.929,
        'q': 0.095,
        'r': 7.587,
        's': 6.327,
        't': 9.356,
        'u': 2.758,
        'v': 0.978,
        'w': 2.560,
        'x': 0.150,
        'y': 1.994,
        'z': 0.077,
        ' ': 18.0,
    }

def letter_ratio(string):
    return sum([LETTER_DISTRIBUTION.get(chr(c).lower(), 0) for c in string]) / len(string)


def xor(msg, key):
    return bytes([c ^ key for c in msg])

def is_probably_text(line, threshold=1.0):
    ratio = letter_ratio(line)
    return  (ratio, ratio > threshold)

def try_keys(line):
    best = {'ratio': 0, 'message': None}
    for i in range(2**8):
        x = xor(line, i)
        ratio, ok = is_probably_text(x)
        if ok and ratio > best['ratio']:
            best['ratio'] = ratio
            best['message'] = ''.join([chr(c) for c in x])
            best['key'] = i
            best['line'] = hexlify(line)

    return best


if __name__ == '__main__':
    with open('6.txt') as f:
        content = f.read()

    decoded = base64.b64decode(content) 
    sizes = sorted(find_keysize(decoded))
    _, ks = sizes[0] 
    blocks = seperate(decoded, int(ks))
    transposed = transpose(blocks)
    key = []
    for block in transposed:
        key.append(try_keys(block)['key'])
    print('Key:', ''.join([chr(c) for c in key]), '\n')
    print(repeating_key_xor(decoded, key).decode('utf-8'))
        
