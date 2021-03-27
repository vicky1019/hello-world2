# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief:

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) # return a strings list

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)'%reprlib.repr(self.text)


if __name__ == "__main__":
    s = Sentence('"i love momo very much" miss say')
    print(s)
    for word in s:
        print(word)

    print(list(s))
    print(s[3])

