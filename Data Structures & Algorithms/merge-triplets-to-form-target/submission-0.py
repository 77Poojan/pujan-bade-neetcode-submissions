class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        a = b = c = 0

        for i, j, k in triplets:
            if i <= x and j <= y and k <= z:
                a = max(a, i)
                b = max(b, j)
                c = max(c, k)

        return [a, b, c] == target
