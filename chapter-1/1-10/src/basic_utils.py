#!/usr/bin/env python

from time import sleep
from random import randint
from multiprocessing import Lock

# 单位: ms
max_io_latency = 5
max_network_latency = 50


class Block:

    def __init__(self, content: str = None):
        assert(type(content) == str)
        assert(len(content) == 1)
        self.content = ord(content)


out_path = './disk.out'

content = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

content_pointer = 0
content_size = len(content)


get_mutex = Lock()
write_mutex = Lock()


def GetBlockFromNet(out_block: Block) -> bool:
    global content_pointer, content_size

    get_mutex.acquire()
    sleep(randint(0, max_network_latency) / 1000)
    if content_pointer >= content_size:
        get_mutex.release()
        return False

    out_block.content = ord(content[content_pointer])
    # print("GetBlockFromNet: ", content[content_pointer])
    content_pointer += 1
    if content_pointer == content_size:
        get_mutex.release()
        return False

    get_mutex.release()
    return True


def WriteBlockToDisk(in_block: Block) -> bool:

    write_mutex.acquire()
    sleep(randint(0, max_io_latency) / 1000)
    try:
        with open(out_path, 'a') as f:
            f.write(chr(in_block.content))
        # print("WriteBlockToDisk: ", chr(in_block.content))
    except IOError:
        write_mutex.release()
        return False

    write_mutex.release()
    return True
