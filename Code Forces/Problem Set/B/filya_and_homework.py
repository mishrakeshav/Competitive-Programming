
def solve():
    n = int(input())
    a = list(map(int,input().split()))
    s = set()
    for i in a:
        s.add(i)
    if len(s) > 3:
        print("NO")
    elif len(s) <= 2:
        print("YES")
    else:
        a = s.pop()
        b = s.pop()
        c = s.pop()
        if (2*a == b + c) or (2*b == a + c) or (2*c == b + a):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()
