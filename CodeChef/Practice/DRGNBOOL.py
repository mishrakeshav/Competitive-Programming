from sys import stdin,stdout
for t in range(int(stdin.readline())):
    N,M = map(int,stdin.readline().split())
    soints = dict() 
    sofloats = dict()
    for i in range(N):
        C,L = map(int,stdin.readline().split())
        if L not in soints:
            soints[L] = C  
        else:
            soints += C  
    for i in range(M):
        C,L = map(int,stdin.readline().split())
        if L not in sofloats:
            sofloats[L] = C  
        else:
            sofloats[L] += C   
    chakras = 0 
    for i in soints:
        if soints[i]-sofloats[i] < 0:
            chakras += sofloats[i] - soints[i]
    stdout.write(str(chakras) + "\n")

