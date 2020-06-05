

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(input()))
    flag = False
    count_min = float("inf")
    count_max = -float("inf")
    for a in range(n):
        flag = False
        i = None
        for b in range(m):
            if table[a][b] == 'G':
                i = b
            
            elif table[a][b] == 'S':
                if i is None:
                    flag = True
                else:
                    count_max = max(count_max, b - i-1)
                    count_min = min(count_min, b - i-1)
    # print(flag)
    if flag:
        print(-1)
    else:
        print(count_max-count_min)
