# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: dict comprehension


DIAL_CIDES = [
    (86, "china"),
    (91, "india"),
    (1, "united states"),
    (7, "russia")
]
# country_code = {country: code for code, country in DIAL_CIDES}
country_code = {country.upper(): code for code, country in DIAL_CIDES}
print(country_code)
# light copy
new_country_code = country_code.copy()
print(new_country_code)
# clear the dict
new_country_code.clear()
print(new_country_code)
# delete country_code['CHINA']
country_code.__delitem__('CHINA')
print(country_code)
# .get(k) method could return a none
print(country_code.get("CHINA"))
# country_code[key] will return a error if there is no key
print(country_code["CHINA"])
# 3-2
# use setdefault to deal with situation where you can not find the key
import sys
import re

WORD_RE = re.compile(r"\w+")
index = {}
with open(sys.argv[1], encoding='utf-8') as file:
    for line_no, line in enumerate(file, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no, line)

            occurrence = index.get(word, [])
            occurrence.append(location)
            index[word] = occurrence

for word in sorted(index, key=str.upper()):
    print(word, index[word])



