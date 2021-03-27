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