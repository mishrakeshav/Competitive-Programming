def solve():
    s = input()
    n = len(s)
    sm = 0 
    for i in s:
        if i == '1':
            sm += 1 
    if s == n:
        print(0)
    elif s[0] == '1' and s[-1] == '1':
        print(sm - 1)
    elif s[0] == '1' and s[-1] == '0' and s == n - 1:
        print(0)
    elif s[0] == '0' and s[-1] == '1' and s == n - 1:
        print(0)
    else:
        print(sm)


    


if __name__ == '__main__':
    for t in range(int(input())):
        solve()