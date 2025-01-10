n = int(input())
arr = list(map(int, input().split()))
numberRead = 0
index = 0
counter = True
while counter:
    for k, i in enumerate(arr):
        numberRead += i
        if numberRead >= n:
            index = k+1
            counter = False
            break
print(index)
