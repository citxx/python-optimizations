#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Artem Tabolin <artemtab@yandex.ru>
# Example output
# heapq: Inserted 1000000 numbers in 0.45422289200359955 seconds
#        Popped 1000000 numbers in 1.504499205009779 seconds
# PriorityQueue: Inserted 1000000 numbers in 2.7594955299864523 seconds
#                Popped 1000000 numbers in 4.9204087990219705 seconds


import heapq
from queue import PriorityQueue
import os
import random
import time

DATA_SIZE = 10 ** 6
DATA = list(range(DATA_SIZE))

def prepare_data():
    random.shuffle(DATA)
    return DATA


def test_heapq():
    data = prepare_data()
    t1 = time.perf_counter()
    h = []
    for x in data:
        heapq.heappush(h, x)
    t2 = time.perf_counter()
    while h:
        heapq.heappop(h)
    t3 = time.perf_counter()
    return t2 - t1, t3 - t2


def test_priority_queue():
    data = prepare_data()
    t1 = time.perf_counter()
    h = PriorityQueue()
    for x in data:
        h.put(x)
    t2 = time.perf_counter()
    while not h.empty():
        h.get()
    t3 = time.perf_counter()
    return t2 - t1, t3 - t2


t_insertions, t_deletions = test_heapq()
print('heapq: Inserted {0} numbers in {1} seconds\n'
      '       Popped {0} numbers in {2} seconds'
      .format(DATA_SIZE, t_insertions, t_deletions))

t_insertions, t_deletions = test_priority_queue()
print('PriorityQueue: Inserted {0} numbers in {1} seconds\n'
      '               Popped {0} numbers in {2} seconds'
      .format(DATA_SIZE, t_insertions, t_deletions))
