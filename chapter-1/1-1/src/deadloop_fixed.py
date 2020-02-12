#!/usr/bin/env python

import multiprocessing

def deadloop_thread(_):

    counter = False

    while True:
        counter = not counter

cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)

params = range(cores)
for _ in pool.imap_unordered(deadloop_thread, params):
    pass