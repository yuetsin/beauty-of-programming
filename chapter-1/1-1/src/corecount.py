#!/usr/bin/env python

import psutil

def count_cpu():
    try:
        return psutil.cpu_count(logical=False)
    except:
        return 1
