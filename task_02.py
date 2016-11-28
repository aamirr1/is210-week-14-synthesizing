#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 14 sythesizing task 02"""

import task_01

def fibo(count):
    """This is to use a list comprehension to wrap it in a list."""
    
    return [num for num in task_01.xfibo(count)]
