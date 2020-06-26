lookup_table = dict()
def solve(x,c):
    if x < 0:
        return 0
    if x in lookup_table:
        return lookup_table[x] 
    else:
        m = float("inf")
        for i in c:
            m = min(solve(x-i, c) + solve(i,c), m)
        lookup_table[x] = m
        return m 

if __name__ == '__main__':
    n, x = map(int,input().split())
    c = list(map(int,input().split()))
    for i in c:
        lookup_table[i] = 1
    print(solve(x,c))