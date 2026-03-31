class Solution:
    def isHappy(self, n: int) -> bool:
        # seen = set()
        # num = n

        # if num == 1:
        #     return True

        # def check(num, summ):
        #     while num:
        #         digit = num % 10
        #         sq_digit = digit * digit
        #         summ += sq_digit
        #         num //= 10
        #     return summ

        
        # while True:
        #     seen.add(num)
        #     num = check(num, 0)
        #     if num in seen:
        #         return False
        #     if num == 1:
        #         return True


        def get_next(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
