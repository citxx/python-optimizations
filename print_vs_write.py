#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Artem Tabolin <artemtab@yandex.ru>

import os
import random
import time

DATA_SIZE = 10 ** 6
FILE_NAME = 'tmp_caiorsg.txt'
DATA = list(range(DATA_SIZE))

def prepare_data():
    random.shuffle(DATA)
    return DATA


def test_print():
    data = prepare_data()
    with open(FILE_NAME, 'w') as f:
        start = time.perf_counter()
        for x in data:
            print(x, file=f)
        elapsed = time.perf_counter() - start
    os.remove(FILE_NAME)
    return elapsed


def test_write():
    data = prepare_data()
    with open(FILE_NAME, 'w') as f:
        start = time.perf_counter()
        for x in data:
            f.write(str(x) + '\n')
        elapsed = time.perf_counter() - start
    os.remove(FILE_NAME)
    return elapsed


elapsed = test_print()
print('Wrote {} numbers using "print(x, file=f)" in {} seconds'
      .format(DATA_SIZE, elapsed))

elapsed = test_write()
print('Wrote {} numbers using "f.write(str(x) + \'\\n\')" in {} seconds'
      .format(DATA_SIZE, elapsed))
