#!/usr/bin/env python

from time import time
from basic_utils import *
from multiprocessing import Queue
from multiprocessing import Lock, Process, Semaphore, Value
# from multiprocessing.sharedctypes import Array, Value

start_time = time()


BUFFER_COUNT = 42
# g_buffer = [Block('\0')] * BUFFER_COUNT
g_buffer = Queue(BUFFER_COUNT)
g_isMoreBlockLeft = Value('i', True)

g_seFull = Semaphore(BUFFER_COUNT)
g_seFull._value = 0

g_seEmpty = Semaphore(BUFFER_COUNT)
g_seEmpty._value = BUFFER_COUNT


def ProcA():
    global g_isMoreBlockLeft
    # ProcA is producer
    while True:
        # print("<proca> g_isMoreBlockLeft: ", g_isMoreBlockLeft.value)
        g_seEmpty.release()
        block = Block('\0')
        g_isMoreBlockLeft.value = GetBlockFromNet(block)
        g_buffer.put(block)
        g_seFull.acquire(True, 0)

        # producer can stop working once g_isMoreBlockLeft = false
        if not g_isMoreBlockLeft.value:
            break


def ProcB():
    global g_isMoreBlockLeft
    # ProbB is consumer
    while True:
        # print("<procb> g_isMoreBlockLeft: ", g_isMoreBlockLeft.value)
        g_seFull.release()
        WriteBlockToDisk(g_buffer.get())
        g_seEmpty.acquire(True, 0)

        # but consumer must wait till g_buffer is empty
        if (not g_isMoreBlockLeft.value) and g_buffer.empty():
            break


g_threadA = Process(target=ProcA)
g_threadB = Process(target=ProcB)

g_threadA.start()
g_threadB.start()

g_threadA.join()
g_threadB.join()

end_time = time()
print("done! time elapsed:", end_time - start_time, "seconds")
