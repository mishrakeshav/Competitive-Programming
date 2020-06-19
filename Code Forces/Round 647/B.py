

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        ans = 1 
        for i in a:
            ans &= i 
        if ans:
            print(ans)
        else:
            print(-1)