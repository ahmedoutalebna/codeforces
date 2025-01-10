k = int(input())
s = input()
filtering = ''.join(set(s))
output = ''
check = False
if len(filtering) == 1:
    print(s)
else:
    for f in filtering:
        ct = s.count(f)

        if ct % k == 0:
            output += f
        else:
            check = True
            break
if check:
    print(-1)
else:
    print(output * k)