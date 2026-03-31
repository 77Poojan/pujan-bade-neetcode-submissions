class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # sol = []
        # res = []
        # n = len(nums)

        # def backtrack(i):
        #     if i == n:
        #         res.append(sol[:])
        #         return

        #     backtrack(i+1)
        #     sol.append(nums[i])
        #     backtrack(i+1)
        #     sol.pop()

        # backtrack(0)

        # return res


        res = []
        
        def backtrack(i, sol):
            res.append(sol[:])

            for j in range(i, len(nums)):
                # if j > i and nums[j] == nums[j - 1]:
                #     continue

                sol.append(nums[j])
                backtrack(j + 1, sol)
                sol.pop()
            
        backtrack(0, [])
        return res