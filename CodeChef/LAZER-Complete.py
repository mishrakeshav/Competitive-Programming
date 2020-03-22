def isolateOneBit(n):
    return n & -n

def getSum(BIT, ind):
    s = 0
    num = ind
    while num > 0:
        s += BIT[num]
        # print(bin(num))
        num -= isolateOneBit(num)
    
    return s

def rangeSum(BIT,l,u):
    uSum = getSum(BIT, u)
    lSum = getSum(BIT,l-1)
    return uSum-lSum

def updateSums(BIT, nBIT, ind, delta):
    while(ind<=nBIT):
        # print(bin(ind))
        BIT[ind] += delta
        ind += isolateOneBit(ind)

#Fenwick tree end

def main():
    t = int(input())
    while t:
        t-=1
        n, q = map(int, input().split())
        pts = list(map(int, input().split()))
        qArr = []
        for i in range(q):
            quer = list(map(int, input().split()))
            quer.append(i)
            qArr.append(quer[:])
        
        ptsArr = []
        for i in range(1,n):
            a = pts[i-1]
            b = pts[i]
            if a>b:
                a,b = b,a
            ptsArr.append((a, b, i))
        # print(ptsArr)
        startArr = sorted(ptsArr[:])
        endArr = sorted(ptsArr[:],key = lambda x: x[1])
        qArr.sort(key=lambda x: x[2])
        
        # Basic setup done
        fenStart = [0 for i in range(n+10)]
        fenEnd = [0 for i in range(n+10)]

        answers = []
        i = 0
        j = 0
        for query in qArr:
            while(i<n-1 and startArr[i][0]<=query[2]):
                updateSums(fenStart,n+1,startArr[i][2],1)
                i += 1
            
            while(j<n-1 and endArr[j][1]<query[2]):
                updateSums(fenEnd,n+1,endArr[j][2],1)
                j += 1
            # print(i,j,query,endArr[j][1])
            st = rangeSum(fenStart,query[0],query[1]-1)
            ed = rangeSum(fenEnd,query[0],query[1]-1)
           
            answers.append((query[3],ed-st))
        answers.sort()
        for i in answers:
            print(-i[1])

if __name__ == "__main__":
    main()