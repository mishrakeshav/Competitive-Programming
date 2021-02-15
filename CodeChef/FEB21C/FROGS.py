from math import ceil
def solve():
    n = int(input())
    w = list(map(int,input().split()))
    l = list(map(int,input().split()))
    sorted_list = []
    for a,b,c in zip(w,l,range(1,n+1)):
        sorted_list.append([a,b,c])
    sorted_list.sort(key = lambda x : x[0])
    ans = 0 
    prev_pos = 0 
    for wi,li,pi in sorted_list:
        diff = prev_pos - pi
        if pi > prev_pos:
            pass 
        else:
            to_jump = abs(diff) + 1 
            hits = ceil(to_jump/li)
            ans += hits
            pi += hits*li
        prev_pos = pi 
    print(ans)

if __name__ == '__main__':
    for i in range(int(input())):
        solve()