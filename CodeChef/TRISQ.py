def no_of_squares(B):
    if B% 2:
        B -= 1 

    if B < 4:
        return 0
    elif B == 4:
        return 1
    return no_of_squares(B-4) + (B-4)//2
for t in range(int(input())):
    B = int(input())
    print(no_of_squares(B))