from collections import deque
n = int(input())
s = deque(input())
decoded_message = [None] * n


if n % 2:
    k = n // 2
    k1 = k - 1
    k2 = k
else:
    k = n // 2 - 1
    k1 = k
    k2 = k + 1
while s:

    if len(s) % 2:
        e = s.popleft()
        decoded_message[k2] = e
        k2 += 1
    else:
        e = s.popleft()
        decoded_message[k1] = e
        k1 -= 1
print("".join(decoded_message))
