#!/usr/bin/env python

from time import time
from basic_utils import *

start_time = time()

buffer = Block('\0')

while True:
    isMoreBlockLeft = GetBlockFromNet(buffer)
    # print("buffer get", buffer.content)
    WriteBlockToDisk(buffer)
    if not isMoreBlockLeft:
        break

end_time = time()

print("done! time elapsed:", end_time - start_time, "seconds")
