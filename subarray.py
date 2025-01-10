def maximumSubarraySum(nums, k):
    #     for i in range(len(nums)):
    #         if i+k <= len(nums):
    #             sl = nums[i:i+k]
    #             if len(sl) == len(set(sl)):
    #                 sliding.append(sum(sl))
    #             else:
    #                 sliding.append(0)
    #     return max(sliding)
    sliding = []
    for i in range(len(nums)):
        if i + k <= len(nums):
            sub = nums[i:i+k]
            sliding.append(sum(sub))
    return sliding

print(maximumSubarraySum([2, 3, 5, 1, 6, 8, 4], 3))
