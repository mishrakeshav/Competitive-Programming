import random

if __name__ == '__main__':
    print(10)
    for i in range(10):
        n = random.randint(1,20)
        a = []
        print(2*n)
        for i in range(n):
            a.append(random.randint(2,300))
        print(*a, end = " ")
        print(*a)
        s = random.shuffle(a)
        print(*a, end = " ")
        print(*a)
