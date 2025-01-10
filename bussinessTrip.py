k = int(input())
months = sorted(list(map(int, input().split())), reverse=True)
minimum = 0
counter = 0
for a in months:
    minimum += a
    counter += 1
    if minimum >= k:
        break
if k == 0:
    print(0)
elif minimum < k:
    print(-1)
else:
    print(counter)