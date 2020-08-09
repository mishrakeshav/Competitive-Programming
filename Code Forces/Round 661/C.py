"""
Problem link:
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    w = list(map(int, input().split()))
    freq = [0]*(51)
    for i in w:
        freq[i] += 1 
    count = 0
    ans = -float('inf')
    for i in range(2,101):
        s = i
        count = 0
        for j in range(1,51):
            if freq[j]:
                if (0 <= s - j <= 50):
                    count += min(freq[j],freq[s - j])
        ans = max(count//2,ans)
    print(ans)


    


    

if __name__ == '__main__':
    for t in range(int(input())):
        solve()
