# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: slice application

"""basic usage"""
l = [i*10 for i in range(7)]
print(l)
print(l[:2])
print(l[2:])

"""object slice"""
s = 'application'
print(s[::2]) # s[a:b:c]  get value between  a and b with step c
print(s[::-1]) # reverse the order
print(s[::-2])

"""+/* usage in sequence"""
print(l*3)
print(l +[80, 90, 100])



