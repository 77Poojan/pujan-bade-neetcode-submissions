class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        import heapq
        heapq.heapify(nums)          # in-place, returns None

        prev = heapq.heappop(nums)
        count, maxx = 1, 1           # first element = streak of 1

        while nums:
            curr = heapq.heappop(nums)
            if curr == prev + 1:
                count += 1
            elif curr == prev:       # duplicate — skip, don't reset
                continue
            else:
                maxx = max(maxx, count)
                count = 1            # reset to 1, not 0

            prev = curr              # advance prev every iteration

        return max(maxx, count) 
            

