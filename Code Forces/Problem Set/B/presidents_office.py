def findPredidentsDesk(room, n, m):
    for i in range(n):
        for j in range(m):
            if room[i][j] == c:
                start = j
                for k in range(start, m):
                    if room[i][k] != c:
                        return (start, k - 1, i)
                return (start, start, i)


def CountColorsInRow(room, row, start, end, x):
    colors = set()
    count = 0
    c = x + '.'
    for i in range(start, end + 1):
        if room[row][i] not in c and room[row][i] not in colors:
            count += 1
            colors.add(room[row][i])

    return count


if __name__ == '__main__':
    n, m, c = map(str, input().split())
    n = int(n)
    m = int(m)
    room = []
    for i in range(n):
        room.append(input())

    start, end, row = findPredidentsDesk(room, n, m)
    count = 0
    colors = set()
    if start != 0:
        if room[row][start - 1] not in str('.' + c):
            set.add(room[row][start - 1])
            count += 1

    if end != m - 1:
        count += int(room[row][end + 1] not in str('.' + c))

    if row != 0:
        count += CountColorsInRow(room, row - 1, start, end, c)

    if row != n - 1:
        count += CountColorsInRow(room, row + 1, start, end, c)

    print(count)
