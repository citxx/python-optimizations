#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artem Tabolin <artemtab@yandex.ru>

import os
import random
import sys
import time

DATA_SIZE = 10 ** 6
FILE_NAME = 'tmp_feocuysg.txt'
DATA = list(range(DATA_SIZE))


original_stdin = None


def prepare_file():
    global original_stdin

    random.shuffle(DATA)
    with open(FILE_NAME, 'w') as f:
        for x in DATA:
            f.write(str(x) + '\n')
    original_stdin, sys.stdin = sys.stdin, open(FILE_NAME)


def cleanup_file():
    global original_stdin

    sys.stdin.close()
    original_stdin, sys.stdin = None, original_stdin
    os.remove(FILE_NAME)


def test_input():
    prepare_file()
    start = time.perf_counter()

    x = 0
    for i in range(DATA_SIZE):
        x += int(input())

    elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


def test_readline():
    prepare_file()
    start = time.perf_counter()

    x = 0
    for i in range(DATA_SIZE):
        x += int(sys.stdin.readline())

    elapsed = time.perf_counter() - start
    cleanup_file()
    return elapsed


elapsed = test_input()
print('Read {} numbers using "int(input())" in {} seconds'
      .format(DATA_SIZE, elapsed))

elapsed = test_readline()
print('Read {} numbers using "int(sys.stdin.readline())" in {} seconds'
      .format(DATA_SIZE, elapsed))
