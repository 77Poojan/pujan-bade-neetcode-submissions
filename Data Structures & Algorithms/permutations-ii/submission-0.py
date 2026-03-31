class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res, sol = [], []
        # used = [False] * len(nums)

        # def backtrack():
        #     if len(sol) == len(nums):
        #         res.append(sol[:])
        #         return

        #     for j in range(len(nums)):
        #         if used[j]:
        #             continue

        #         if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
        #             continue

        #         used[j] = True
        #         sol.append(nums[j])
        #         backtrack()
        #         sol.pop()
        #         used[j] = False

        # sol = []
        # backtrack()
        # return res


        res = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return

            for i in range(len(nums)):
                if nums[i] != float("-inf"):
                    perm.append(nums[i])
                    nums[i] = float("-inf")
                    backtrack(perm)
                    nums[i] = perm[-1]
                    perm.pop()

        backtrack([])
        return list(res)