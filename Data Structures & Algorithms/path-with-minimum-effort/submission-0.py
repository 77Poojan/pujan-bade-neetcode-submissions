class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]] ##[diff, r, c]
        traces = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))
                        
            if (r, c) == (rows - 1, cols - 1):
                return diff

            for x, y in traces:
                rx, cy = r + x, y + c
                if rx < 0 or cy < 0 \
                    or rx == rows or cy == cols \
                    or (rx, cy) in visited:
                    continue

                new_diff = max(diff, abs(heights[r][c] - heights[rx][cy]))
                heapq.heappush(minHeap, [new_diff, rx, cy])

        

        


