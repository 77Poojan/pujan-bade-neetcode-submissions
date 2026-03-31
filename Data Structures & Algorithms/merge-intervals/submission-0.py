class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 1
        res = []
        curr = intervals[0]
        
        
        for i in range(1, n):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(intervals[i][1], curr[1])
            else:
                res.append(curr)
                curr = intervals[i]

        res.append(curr)
        return res