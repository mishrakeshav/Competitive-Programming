for r in range(int(input())):
    r, c = map(int, input().split())
    wall = []
    for i in range(r):
        wall.append(input())

    elements = []
    isStable = False
    for i in wall[-1]:
        elements.append([{i}, 0, i])

    for i in range(r - 2, -1, -1):
        for j in range(c):
            if wall[i][j] == elements[j][2]:
                continue

            if wall[i][j] in elements[j][0]:
                isStable = False
                break

            elements[j][1] = elements[j][2]
            elements[j][2] = wall[i][j]

    print("isStable= ", isStable)
    print(elements)
