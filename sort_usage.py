# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: compare sorted and temp_list.sort()
p = print

"""sorted"""
fruits = ["grape", "raspberry", "apple", "bnana"]
p(sorted(fruits))
p(fruits)
p(sorted(fruits, reverse=True))
p(sorted(fruits, key=len))

"""temp_list.sort()"""
p(fruits.sort())
p(fruits)

"""bisect"""
import bisect
import sys
import random

HAYSTACK = [i for i in range(14)]
p(HAYSTACK)
NEEDLES = []
