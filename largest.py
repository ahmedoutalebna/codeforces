from collections import Counter


def largestGoodInteger(num):
    counterNum = Counter(num)
    arr = []
    for k in num:
        if k * 3 in num:
            val = k * 3
            if val not in arr: arr.append(val)
    return max(arr)




print(largestGoodInteger("6777133339"))