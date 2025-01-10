from collections import defaultdict


def leastBricks(wall):
    bricks = []
    freq = defaultdict(int)
    for row in wall:
        rowSum = row[0]
        for j in range(1, len(row)):
            freq[rowSum] += 1
            rowSum += row[j]
    return len(wall) - max(freq.values() or [0])



print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))

# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         freq = defaultdict(int)
#         for row in wall:
#             rowSum = row[0]
#             for j in range(1, len(row)):
#                 freq[rowSum] += 1
#                 rowSum += row[j]
#         return len(wall) - max(freq.values() or [0])