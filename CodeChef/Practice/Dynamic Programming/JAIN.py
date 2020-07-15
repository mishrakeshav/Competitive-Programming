"""
https://www.codechef.com/problems/JAIN
Type: Dynamic Programming
"""

def solve():
    n = int(input())
    freq = dict()
    for i in range(32):
        freq[i] = 0 
    for i in range(n):
        s = set(input())
        si = 0
        if 'a' in s:
            si += 1<<0
        if 'e' in s:
            si += 1<<1 
        if 'i' in s:
            si += 1<<2 
        if 'o' in s:
            si += 1<<3 
        if 'u' in s:
            si += 1<<4 
        freq[si] += 1
    ans = 0
    for i in range(1,32):
        for j in range(i+1,32):
            if i|j == 31:
                ans += freq[i]*freq[j]
    
    if freq[31]:
        ans += (freq[31]*(freq[31]-1))//2
    print(ans)


if __name__ == '__main__':
    for t in range(int(input())):
        solve()