class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_maxx, curr_minn = 1, 1
        res = max(nums)

        for num in nums:
            if num == 0:
                curr_maxx = 1 
                curr_minn = 1
                continue

            temp = curr_maxx * num
            curr_maxx = max(temp, num * curr_minn, num)
            curr_minn = min(temp, num * curr_minn, num)
            res = max(res, curr_maxx)
            
        return res