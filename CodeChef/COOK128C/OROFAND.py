def cal(arr):
    for i in arr:
        k = i 
        j = 0
        while k:
            if k%2:
                bits[j] += 1 
            j += 1 
            k >>=1 
 
def remove(val):
    k = val 
    j = 0
    while k:
        if k%2:
            bits[j] -= 1 
        j += 1 
        k >>=1 

def add(val):
    k = val 
    j = 0
    while k:
        if k%2:
            bits[j] += 1 
        j += 1 
        k >>=1 

def value():
    k = 1
    ans = 0 
    for i in range(len(bits)):
        if bits[i] >= 1:
            ans += k
        k *= 2  
    return ans 

for t in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    bits = [0 for i in range(64)]
    cal(arr)
    ans1 = value()
    print(ans1)
    for i in range(q):
        x,v = map(int,input().split())
        prev = arr[x-1]
        remove(prev)
        add(v)
        ans1 = value()
        print(ans1)
        arr[x-1] = v


