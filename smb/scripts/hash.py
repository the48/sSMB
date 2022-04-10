#!/usr/bin/env python3

import hashlib

def make_md5(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, "rb") as f:
        for x in iter(lambda: f.read(4096), b""):
            hash_md5.update(x)
    print(hash_md5.hexdigest())

make_md5('./asd.py')
