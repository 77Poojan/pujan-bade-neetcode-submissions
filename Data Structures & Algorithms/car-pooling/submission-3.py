class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = float("inf")
        end = float("-inf")

        for _, s, d in trips:
            start = min(start, s)
            end = max(end, d)

        changes = [0] * (end + 1)

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers

        curr = 0
        for i in range(len(changes)):
            curr += changes[i]
            if curr > capacity:
                return False

        return True