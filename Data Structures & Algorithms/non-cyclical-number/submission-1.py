class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n

        if num == 1:
            return True

        def check(num, summ):
            while num:
                digit = num % 10
                sq_digit = digit * digit
                summ += sq_digit
                num //= 10
            return summ

        
        while True:
            seen.add(num)
            num = check(num, 0)
            if num in seen:
                return False
            if num == 1:
                return True
