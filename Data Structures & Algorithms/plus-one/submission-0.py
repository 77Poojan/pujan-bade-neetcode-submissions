class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        nums = digits[0]
        s = []

        for digit in digits[1:]:
            nums = nums * 10 + digit
        
        nums += 1

        for ch in str(nums):
            s.append(int(ch))

        return s

