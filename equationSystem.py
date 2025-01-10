n, m = map(int, input().split())
counter = 0
if n == m == 1:
    print(2)
elif n == m == 2:
    print(1)
else:
    for i in range(n // 2 + 1):
        for j in range(m // 2 + 1):
            if ((i ** 2) + j) == n and (i + (j ** 2)) == m:
                counter += 1
    print(counter)