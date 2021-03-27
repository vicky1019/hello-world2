# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: listcomps is short for list comprehension

# example 1
"""change a strings to Unicode list"""
symbols = '$%&*#@'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

"""listcomps"""
codes_0 = [ord(symbol) for symbol in symbols]
print(codes)

# example 2
"""include if else in listcomps"""
beyond_ascii = [ord(s) for s in symbols if ord(s) > 38]
print(beyond_ascii)