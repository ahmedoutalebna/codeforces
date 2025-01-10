from collections import Counter
def sortColors(nums):
    # output = []
    # # solve this without using sort built in functions
    # for n in nums:
    #     if n == 0:
    #         output.insert(0, n)
    #     if n == 1:
    #         k = output.index(2)
    #         output.insert(k, n)
    #     if n == 2:
    #         output.append(n)
    # return output
    zeros_idx = []
    ones_idx = []
    two_idx = []
    for l, n in enumerate(nums):
        if n == 0: zeros_idx.append(l)
        if n == 1: ones_idx.append(l)
        if n == 2: two_idx.append(l)

            

print(sortColors([2,0,2,1,1,0]))
# the output must be : [0, 0, 1, 1, 2, 2]
