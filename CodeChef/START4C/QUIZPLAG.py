def getlist():
    return list(map(int,input().split()))
    
def getInt():
    return int(input())
from collections import Counter
for t in range(getInt()):
    n,m,k = getlist()
    l = Counter(getlist())
    ans = []
    for i in range(1,n+1):
        if l[i] > 1:
            ans.append(i)
    
    print(len(ans),*ans)



    
