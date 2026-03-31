class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        summ1, summ2 = 0, 0
        minn = float('inf')
        maxx = float('-inf')
        minn_positive = float('inf')

        for num in nums:
            summ1 += num

            if num < minn:
                minn = num
                
            if num >= 0 and num < minn_positive:
                minn_positive = num

            if num > maxx:
                maxx = num

        if minn > 0 and maxx > 0:
            for i in range(minn, maxx+1):
                summ2 += i
        
        if minn_positive == float('inf') or minn_positive > 1:
                return 1
            
        if summ1 == summ2:
            return maxx + 1
        
        else:
            seen = set(nums)
            for i in range(minn_positive, maxx+2):
                if i not in seen:
                    return i