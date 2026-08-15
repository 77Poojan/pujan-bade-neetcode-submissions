class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                k, l = j + 1, n - 1
                while k < l:
                    summ = nums[i] + nums[j] + nums[k] + nums[l]
                    if summ < target:
                        k += 1
                    elif summ > target:
                        l -= 1
                    else:
                        if [nums[i], nums[j], nums[k], nums[l]] not in triplets:
                            triplets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]: k += 1
                        while k < l and nums[l] == nums[l+1]: l -= 1

        return triplets