for t in range(int(input())):
    N = int(input())
    S = input()
    team1 = 0 
    n1 = N
    n2 = N
    team2 = 0 
    for i in range(2*N):
        if i%2 == 0 :
            team1 += int(S[i])
            n1 -=1
        else:
            team2 += int(S[i])
            n2 -= 1

        if team1 < team2:
            if team2 - team1 > n1:
                print(i+1)
                break
        elif team2 < team1:
            if team1 - team2 > n2:
                print(i+1)
                break 
    else:
        print(2*N)