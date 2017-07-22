#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artem Tabolin <artemtab@yandex.ru>

import os
import random
import time

DATA_SIZE = 10 ** 7
DATA = list(range(DATA_SIZE))


def prepare_data():
    random.shuffle(DATA)
    return DATA


def main():
    data = prepare_data()
    start = time.perf_counter()

    a = 0
    for i in range(DATA_SIZE):
        a += data[i] if i&1 else -data[i]

    return time.perf_counter() - start


# Top-level
data = prepare_data()
start = time.perf_counter()

a = 0
for i in range(DATA_SIZE):
    a += data[i] if i&1 else -data[i]

elapsed = time.perf_counter() - start
print('Sum of {} numbers on module level in {} seconds'
      .format(DATA_SIZE, elapsed))


# Function
elapsed = main()
print('Sum of {} numbers on function level in {} seconds'
      .format(DATA_SIZE, elapsed))
