class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        curr_end = intervals[0][1]
        n = len(intervals)
        count = 0
   
        for i in range(1, n):
            start, end = intervals[i]
            if start < curr_end:
                count += 1
                curr_end = min(curr_end, end)

            else:
                curr_end = end

 
        return count