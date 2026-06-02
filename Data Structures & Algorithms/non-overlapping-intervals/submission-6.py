class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        curr_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < curr_end:
                count += 1
                curr_end = min(curr_end, end)
            else:
                curr_end = end

        return count