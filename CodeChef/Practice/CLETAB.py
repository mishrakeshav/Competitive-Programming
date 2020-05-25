from collections import Counter


if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        c = list(map(int, input().split()))
        table = set()
        count = 0
        for i in range(m):
            customer = c[i]
            if customer in table:
                continue
            count += 1

            if len(table) < n:
                table.add(customer)
                continue
            temp = table.copy()
            for j in range(i + 1, m):
                if len(temp) == 1:
                    break

                if c[j] in temp:
                    temp.remove(c[j])
            a = temp.pop()
            table.remove(a)
            table.add(customer)
        print(count)
