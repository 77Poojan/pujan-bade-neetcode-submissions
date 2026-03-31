from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l, r = 0, 0
        n = len(nums)
        output = []

        while r < n:
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()
            
            if (r + 1) >= k:
                output.append(nums[dq[0]])
                l += 1
            r += 1

        return output