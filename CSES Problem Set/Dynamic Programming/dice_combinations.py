
lookup_table = [None]*(10**6 + 1)
def dice_combinations(n):
    if n < 0:
        return 0
    if lookup_table[n]:
        return lookup_table[n]
    if n == 1:
        lookup_table[n] = 1 
        return lookup_table[n]
    elif n == 2:
        lookup_table[n] = 2 
        return lookup_table[n]
    elif n == 3:
        lookup_table[n] = 4
        return lookup_table[n]
    elif n == 4:
        lookup_table[n] = 8
        return lookup_table[n]
    elif n == 5:
        lookup_table[n] = 16 
        return lookup_table[n]
    elif n == 6:
        lookup_table[n] = 32
        return lookup_table[n]
    else:
        s = 0
        for i in range(1,7):
            s += dice_combinations(n-i)
        return s 


def solve():
    n = int(input())
    print(dice_combinations(n))


if __name__ == '__main__':
    solve()