def seperate_time(input_time):
    H, M, Z = int(input_time[:2]), int(input_time[3:5]), input_time[6:]
    if Z == 'AM':
        H %= 12    
    elif Z == 'PM':
        if H != 12:
            H += 12 
    H *= 60
    H += M 
    return H 

if __name__ == '__main__':
    for t in range(int(input())):
        P = seperate_time(input())
        N = int(input())
        slots = []
        for i in range(N):
            S = input()
            T1, T2 = seperate_time(S[:8]), seperate_time(S[9:])
            slots.append([T1,T2])
        ans = []
        for slot in slots:
            l,r = slot
            if l <= P <= r:
                ans.append('1')
            elif l > r and r >= P:
                ans.append('1')
            else:
                ans.append('0')
        print("".join(ans))


        

        