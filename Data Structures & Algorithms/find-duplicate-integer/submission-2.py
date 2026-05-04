class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        ## Intersections
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        ## Equidistance
        slow_nxt = 0
        while True:
            slow = nums[slow]
            slow_nxt = nums[slow_nxt]
            if slow == slow_nxt:
                return slow