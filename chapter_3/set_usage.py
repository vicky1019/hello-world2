# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief:

set1 = {"word", "name","class","china", "big","light","peak"}
set2 = {"word", "name","class","china", "big","light","country","side walk","water"}
# question: calculate the the amount of words which are in set1 meanwhile in set2

count = len(set1 & set2)
print(count)

# traditional way
count = 0
for n in set1:
    if n in set2:
        count += 1
print(count)


list1 = ["word", "name","class","china", "big","light","peak"]
list2 = ["word", "name","class","china", "big","light","country","side walk","water"]
count = len(set(list1) & set(list2))
print(count)


# faster way to creat a set
# normal way
a = set([1, 2, 3])
# better way
b = {1, 2, 3}
print(a)
print(b)


"""set comprehension"""
from unicodedata import name
c = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i), '')}
print(c)