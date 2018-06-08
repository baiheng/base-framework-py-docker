#!/bin/env python
# -*-coding:utf-8-*-

import os
import asyncio
import time
import requests


async def c(p):
    pid = os.getpid()
    print("pid", p, pid)
    await asyncio.sleep(1)
    return p


async def t(p):
    print("{} - start".format(p))
    q = await c(p)
    print("{} - end".format(p))

def cc(p):
    pid = os.getpid()
    print("in cc pid", p, pid)
    r = requests.get("https://www.google.com/")
    print("in cc end", r.status_code)
    return p

async def tt(loop):
    a = loop.run_in_executor(None, cc, 10)
    b = loop.run_in_executor(None, cc, 11)
    await a
    await b


print(asyncio.iscoroutinefunction(t))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    tt(loop),
    t(1),
    t(2),
    t(3),
    ))
loop.close()
