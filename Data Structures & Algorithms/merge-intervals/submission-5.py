from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curr = intervals[0]
        n = len(intervals)

        for i in range(1, n):
            print(intervals[i])
            if intervals[i][0] <= curr[1]:
                curr[1]= max(curr[1], intervals[i][1])

            else:
                res.append(curr)
                curr = intervals[i]

        res.append(curr)
        return res