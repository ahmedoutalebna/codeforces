def longestConsecutive(nums):
    arr = sorted(set(nums))
    print(arr)
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1
    output = 1
    final = []
    for k in range(1, len(arr)):
        if arr[k] - arr[k - 1] == 1:
            output += 1
            final.append(output)
        else:
            final.append(output)
            output = 1
    if len(final) == 0: return output
    else: return max(final)

print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))