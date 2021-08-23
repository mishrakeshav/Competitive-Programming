from math import ceil,floor, factorial as fact, inf 
from copy import deepcopy
def get_list():
    return list(map(int,input().split()))
def get_int():
    return int(input())


for t in range(get_int()):
    s = get_int()
    c = 1 
    m = 0 
    while c < len(s):
        if s[c] == 'x':
            if s[c-1] == 'y':
                c += 2 
                m += 1 
            else:
                c += 1 
        elif s[c] == 'y':
            if s[c-1] == 'x':
                c += 2 
                m += 1 
            else:
                c += 1 
    print(m)