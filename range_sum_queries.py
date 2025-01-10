class NumArray:
    output = [None]
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, left, right):
        for idx, num in enumerate(self.nums):
            if idx == 0:
                val = sum(num[0][left: right+1])
                self.output.append(val)





obj = NumArray([[[-2, 0, 3, -5, 2, -1]],
                [0, 2],
                [2, 5],
                [0, 5]])
param_1 = obj.sumRange(0,2)

