func eraseOverlapIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    currEnd := intervals[0][1]
	count := 0

    for _, interval := range intervals[1:] {
        start, end := interval[0], interval[1]

        if start < currEnd {
            currEnd = min(end, currEnd)
			count += 1
        } else {
            currEnd = end
        }
    }
    return count
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

