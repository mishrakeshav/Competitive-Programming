def modarray(A, N, K):
    if(K > 3 * N):
        if N % 2 != 0:
            A[N // 2] = 0
    x = K % (N * 3)
    for i in range(x):
        a = i % N
        b = N - i % N - 1
        A[a] = A[a] ^ A[b]


for t in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    modarray(A, N, K)
    for i in A:
        print(i, end=" ")
    print()
