def pivot_index(nums):
    for i in range(len(nums)):
        if i == 0:
            sumNumber = sum(nums[i+1:])
            if sumNumber == 0:
                return 0
        if i > 0 and i + 1 <= len(nums) -1:
            right = sum(nums[:i])
            left = sum(nums[i+1:])
            if left == right:
                return i
        if i == len(nums) - 1:
            sums = sum(nums[:i])
            if sums == nums[i]:
                return i
            else:
                return -1



print(pivot_index([2, 1, -1]))

