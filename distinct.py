n = int(input())
checked = False
while not checked:
    n += 1
    arr = [str(k) for k in str(n)]
    if len(arr) == len(set(arr)):
        print(n)
        checked = True
        break
