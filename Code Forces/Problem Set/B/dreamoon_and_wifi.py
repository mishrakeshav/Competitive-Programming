if __name__ == '__main__':
    a = input()
    b = input()
    p1 = 0
    for i in a:
        if i == '+':
            p1 += 1
        else:
            p1 -= 1

    count = 0
    p2 = 0
    for i in b:
        if i == '+':
            p2 += 1
        elif i == '-':
            p2 -= 1
        else:
            count += 1
    s = 0
    if count == 0:
        if p2 == p1:
            print("%.12f" % 1)
        else:
            print("%.12f" % 0)
    else:

        for i in range(2**count):
            p = 0
            k = i
            plus = 0
            while k:
                if k % 2:
                    plus += 1
                k //= 2
            minus = count - plus
            # print(p)
            if p2 + plus - minus == p1:
                s += 1
        j = s / (2**count)
        print("%.12f" % j)
