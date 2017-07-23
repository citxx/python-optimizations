#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artem Tabolin <artemtab@yandex.ru>
# Example output:
# Read 1000000 numbers into array using "a.append(int(f.readline()))" in 0.5692962329994771 seconds
# Read 1000000 numbers into array using "a[i] = int(f.readline())" in 0.5054713299978175 seconds
# Read 1000000 numbers into array using "a = [int(f.readline()) for i in range(n)]" in 0.5023784420045558 seconds

import os
import random
import time

DATA_SIZE = 10 ** 6
FILE_NAME = 'tmp_fovbeas.txt'
DATA = list(range(DATA_SIZE))


def prepare_file():
    random.shuffle(DATA)
    with open(FILE_NAME, 'w') as f:
        for x in DATA:
            f.write(str(x) + '\n')
    return open(FILE_NAME)


def cleanup_file():
    os.remove(FILE_NAME)


def test_append():
    with prepare_file() as f:
        start = time.perf_counter()

        a = []
        for i in range(DATA_SIZE):
            a.append(int(f.readline()))

        elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


def test_assign():
    with prepare_file() as f:
        start = time.perf_counter()

        a = [0] * DATA_SIZE
        for i in range(DATA_SIZE):
            a[i] = int(f.readline())

        elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


def test_generator():
    with prepare_file() as f:
        start = time.perf_counter()

        a = [int(f.readline()) for i in range(DATA_SIZE)]

        elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


elapsed = test_append()
print('Read {} numbers into array using "a.append(int(f.readline()))" in {} seconds'
      .format(DATA_SIZE, elapsed))

elapsed = test_assign()
print('Read {} numbers into array using "a[i] = int(f.readline())" in {} seconds'
      .format(DATA_SIZE, elapsed))

elapsed = test_generator()
print('Read {} numbers into array using "a = [int(f.readline()) for i in range(n)]" in {} seconds'
      .format(DATA_SIZE, elapsed))
