class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # Count sort if needed O(n)
        l, r, res = 0, len(people) - 1, 0
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res