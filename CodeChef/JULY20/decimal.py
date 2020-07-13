def getN(n):
    n /= 1
    exp, man = str(n).split('.')
    exp = int(exp[0])
    man = int(man[0])
    if man:
        return man
    if exp:
        return exp
    
    return 0

for t in range(int(input())):
    n = int(input())
    i = 0
    div = list(map(int, input().split()))
    arr = []
    n = getN(n)
    memo = set()
    while True:
        if (n, div[i%3]) in memo:
            break
        else:
            memo.add((n, div[i%3]))
            arr.append(n)
            n = getN(n/div[i%3])
            i += 1
    
    idx = arr.index(n)
    rep = arr[idx:]
    const = arr[:idx]
    print(rep)
    for q in range(int(input())):
        idx = int(input())
        if idx > len(const):
            idx -= len(const)
            idx %= len(rep)
            print(rep[idx-1])
        else:
            print(const[idx-1])