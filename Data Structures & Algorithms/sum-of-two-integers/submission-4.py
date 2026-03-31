class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            without_carry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = without_carry, carry

        # handle negative numbers
        return a if a <= INT_MAX else  a - (1 << 32)