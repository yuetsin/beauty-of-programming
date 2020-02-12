#!/usr/bin/env python

import sys
import time
import psutil
import threading
import multiprocessing

cores = multiprocessing.cpu_count()
freq = psutil.cpu_freq()[2] * 1000000

target_percentage = 50.0

ratio = 0.01
should_busy = True

def check_busy_state():
    global should_busy

    v = psutil.cpu_percent(1)
    # print(v)
    if v <= target_percentage:
        # print("Busy!")
        should_busy = True
    else:
        # print("Free!")
        should_busy = False

def deadloop_thread(_):
    global should_busy

    t = True
    while True:
        thread = threading.Thread(target=check_busy_state,args=())
        thread.start()
        
        if should_busy:
            for _ in range(int(freq * ratio)):
                pass
        else:
            time.sleep(0.01)

pool = multiprocessing.Pool(processes=cores)

params = range(cores)
for _ in pool.imap_unordered(deadloop_thread, params):
    pass