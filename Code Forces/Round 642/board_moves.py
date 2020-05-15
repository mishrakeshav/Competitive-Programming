for t in range(int(input())):
    n = int(input())
    k = n//2 
    ans = ((k*(k+1)*(2*k+1))//6)*8
    print(ans)