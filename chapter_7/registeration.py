# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief:

registry = []

def register(func):
    print('running register(%s)'% func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
