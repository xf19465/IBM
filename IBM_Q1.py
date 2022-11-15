import numpy as np

a = int(input())
b = input()
c = int(input())
d = input()

def X_to_num(size):
    XS_split = [*size]
    N = len(XS_split)
    if XS_split[-1] == 'S':
        if N > 1:
            return -(N-1)
        else:
            return -1
    if XS_split[-1] == 'M':
        return 0
    if XS_split[-1] == 'L':
        if N > 1:
            return N-1
        else:
            return 1

def all_shirt(data):
    no_list = [X_to_num(i) for i in data]
    no_list.sort()
    no_list = list(filter((None).__ne__, no_list))
    print(no_list)
    return no_list

def check(a, b, c ,d):
    if c > a:
        print('No')
    else:
        b = all_shirt(b)
        d = all_shirt(d)
        if b[-c:] >= d[-c:]:
            print('Yes')
        else:
            print('No')


check(a, b, c, d)