class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        c = Counter(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])

            for num in c:
                if c[num] > 0:
                    c[num] -= 1
                    sol.append(num)
                    backtrack(i+1)
                    sol.pop()
                    c[num] += 1

        backtrack(0)
        return res
    

        # res = set()

        # def backtrack(perm):
        #     if len(perm) == len(nums):
        #         res.add(tuple(perm))
        #         return

        #     for i in range(len(nums)):
        #         if nums[i] != float("-inf"):
        #             perm.append(nums[i])
        #             nums[i] = float("-inf")
        #             backtrack(perm)
        #             nums[i] = perm[-1]
        #             perm.pop()

        # backtrack([])
        # return list(res)