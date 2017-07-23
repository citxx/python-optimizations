#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artem Tabolin <artemtab@yandex.ru>
# Example output:
# Read 10000000 numbers using "list(map(int, f.readline().split()))" in 1.7740818100028264 seconds
# Read 10000000 numbers using "[int(x) for x in f.readline().split()]" in 2.1468002189976687 seconds


import os
import random
import time

DATA_SIZE = 10 ** 7
FILE_NAME = 'tmp_asvrvads.txt'
DATA = list(range(DATA_SIZE))


def prepare_file():
    random.shuffle(DATA)
    with open(FILE_NAME, 'w') as f:
        for x in DATA:
            f.write(str(x) + ' ')
    return open(FILE_NAME)


def cleanup_file():
    os.remove(FILE_NAME)


def test_map():
    with prepare_file() as f:
        start = time.perf_counter()

        a = list(map(int, f.readline().split()))

        elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


def test_generator():
    with prepare_file() as f:
        start = time.perf_counter()

        a = [int(x) for x in f.readline().split()]

        elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


elapsed = test_map()
print('Read {} numbers using "list(map(int, f.readline().split()))" in {} seconds'
      .format(DATA_SIZE, elapsed))

elapsed = test_generator()
print('Read {} numbers using "[int(x) for x in f.readline().split()]" in {} seconds'
      .format(DATA_SIZE, elapsed))
