

if __name__ == '__main__':
    n, m, x = map(int, input().split())
    keyboard = []
    for i in range(n):
        keyboard.append(input())
    q = int(input())
    text = input()

    shift_keys = []
    cost = dict()
    for i in range(n):
        for j in range(m):
            if keyboard[i][j] == 'S':
                shift_keys.append((i, j))
            else:
                cost[keyboard[i][j]] = 0

    if len(shift_keys) > 0:
        for i in range(n):
            for j in range(m):
                if keyboard[i][j] != 'S':
                    distance = min((i - si)**2 + (j - sj) **
                                   2 for si, sj in shift_keys)
                    letter = keyboard[i][j].upper()
                    if distance <= x**2:
                        cost[letter] = 0
                    elif letter not in cost:
                        cost[letter] = 1

    result = 0
    for letter in text:
        if letter in cost:
            result += cost[letter]
        else:
            result = -1
            break
    print(result)
