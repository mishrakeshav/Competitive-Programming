"""
https://www.codechef.com/LRNDSA07/problems/SUBINC 
Type: Dynamic Programming

"""

def solve():
    ans = 0 
    count = 1 
    
    for i in range(1,n):
        if a[i-1] <= a[i]:
            count += 1 
            
        else:
            if count > 1:
                ans += count*(count+1)//2 
                
            else:
                ans += 1 
            count = 1
    if count > 1:
        ans += count*(count + 1)//2
    else:
        ans += 1 
    
            
            
    print(ans)


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        solve()