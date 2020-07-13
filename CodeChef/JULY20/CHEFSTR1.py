

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        s = list(map(int,input().split()))
        count = 0
        for i in range(1,n):
            count += abs(s[i-1] - s[i]) - 1
        print(count)
         