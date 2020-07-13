def solve():
    n = int(input())
    v = list(map(int, input().split()))
    count = 0
    

    l = -float("inf")
    for i in range(n-1):
        if v[i] > l and v[i] > v[i+1]:
            count += 1 
            l = v[i]
        if i == 0:
            l = v[0]
    if v[-1] > l:
        count += 1
    return count

if __name__ == '__main__':
    for t in range(int(input())):
        print("Case #{}: {}".format(t+1,solve()))