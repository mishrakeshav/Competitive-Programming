#python3
for t in range(int(input())):
    count = 0 
    s,w1,w2,w3 = map(int,input().split())
    if((w1+w2+w3)<=s):
        count = 1 
    elif((w1+w2)<=s):
        if(w3 <= s):
            count = 2 
        else:
            count = 1 
    elif((w2+w3)<=s):
        if(w3 <= s):
            count = 2 
        else:
            count = 1 
    elif(w1 <= s and w2 <= s and w3 <= s):
        count = 3 
    elif(w1>s  and w3 > s):
        count = 0 
    print(count)

#score:100
    
        
