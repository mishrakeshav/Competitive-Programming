"""
Problem link: 
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')
from collections import Counter 

# Constants 
YES = 'YES'
NO = 'NO'
yes = 'yes'
no = 'no'
true = 'true'
false = 'false'




def solve(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0 
    max_count = 0 
    prev = None
    prev_element = a[0]
    for i in range(1,n):
        if prev is not None:
            if prev == (prev_element - a[i]):
                count += 1
            else:
                max_count = max(count,max_count)
                count = 1 
            prev = prev_element - a[i]
            prev_element = a[i] 
        else:
            prev = prev_element - a[i]
            prev_element = a[i]
            count += 1 
    max_count = max(count, max_count)
    print('Case #%d: %d'%(t, max_count+1))

        
    

if __name__ == '__main__':
    for t in range(int(input())):
        ans = solve(t+1)
        
    