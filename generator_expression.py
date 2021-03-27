# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: genexps is short for generator expression,initial tuple,array,sequence

symbols = '$%&*#@'
res = tuple(ord(symbol) for symbol in symbols)
print(res)

import array
res1 = array.array("I", (ord(symbol) for symbol in symbols))
print(res1)




