from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    times = []
    m = -float('inf')
    for i in range(n):
        a,b = map(int,input().split())
        m = max(b,m)
        times.append([a,1])
        times.append([b,-1])
    times.sort()
    

    
    max_customers = 0
    temp = 0
    for time in times:
        temp += time[1]
        max_customers = max(max_customers,temp)
    
    print(max_customers)

    
        
    