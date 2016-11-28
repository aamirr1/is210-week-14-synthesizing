#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Synthesizing task number 1"""

def xfibo(count):
    """This is to create a new Fibonacci sequence generator."""
    
    iteration = 0
    beginnum, endnum = 0, 1
    while iteration < count:
        yield beginnum
        beginnum, endnum = endnum, beginnum + endnum
        iteration += 1
