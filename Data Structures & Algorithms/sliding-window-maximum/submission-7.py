from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        for r in range(len(nums)):
            # Remove smaller values from the back
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            # Remove index outside the window
            if queue[0] <= r - k:
                queue.popleft()

            # Window has reached size k
            if r >= k - 1:
                res.append(nums[queue[0]])

        return res