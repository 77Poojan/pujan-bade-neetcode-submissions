class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ < 0:
                    j += 1
                elif summ > 0:
                    k -= 1
                else:
                    arr.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while nums[j-1] == nums[j] and j < k: j += 1
                    while nums[k+1] == nums[k] and j < k: k -= 1      
        return arr