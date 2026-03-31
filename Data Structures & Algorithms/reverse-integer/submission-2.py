class Solution:
    def reverse(self, x: int) -> int:
        if not x or x == 0:
            return 0
        
        u = False
        if x < 0:
            x = -x
            u = True

        temp = 0
        rem = 0
        rev_digit = 0

        while True:
            temp = x % 10
            rev_digit = rem * 10 + temp
            x //= 10
            rem = rev_digit
            if x == 0:
                break
        
        if u:
            rev_digit = -rev_digit
        
        if rev_digit < -2**31 or rev_digit > 2**31 - 1:
            return 0
        
        return rev_digit