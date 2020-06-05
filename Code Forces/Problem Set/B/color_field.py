

if __name__ == '__main__':
    n, m, k, t = map(int, input().split())
    waste_lands = []
    waste = set()
    for i in range(k):
        a, b = map(int, input().split())
        waste.add((a, b))
        waste_lands.append((a, b))
    waste_lands.sort()
    Plants = ['Carrots', 'Kiwis', 'Grapes']

    for i in range(t):
        a, b = map(int, input().split())
        if (a, b) in waste:
            print("Waste")
            continue
        cellno = (a - 1) * m + b
        c = 0
        for i in waste_lands:
            if i < (a, b):
                c += 1
        cellno -= c
        cellno = cellno % 3
        print(Plants[cellno - 1])
