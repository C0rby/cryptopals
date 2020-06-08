#!/usr/bin/env python3
import math


def seperate(msg, blocksize):
    blockcount = math.ceil(len(msg)/blocksize)
    blocks = []
    for i in range(blockcount):
        blocks.append(msg[i*blocksize: i*blocksize+blocksize]) 
    return blocks

def detect_ecb(blocks):
    start_len = len(blocks)
    blocks = list(set(blocks))
    return start_len != len(blocks)

if __name__ == '__main__':
    with open('8.txt') as f:
        for i, line in enumerate(f):
            line = line.strip()
            blocks = seperate(line.strip(), 32)
            if detect_ecb(blocks):
                print('Line ', i + 1)

