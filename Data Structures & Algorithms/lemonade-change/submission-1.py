class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5:
            return False

        s = {5: 1, 10: 0, 20: 0}
        
        for idx, bill in enumerate(bills[1:]):

            if bill == 20:
                if s[10] == 0 and s[5] >= 3:
                    s[5] -= 3

                else:
                    s[10] -= 1
                    s[5] -= 1

                if s[10] < 0 or s[5] < 0:
                    return False

                s[20] += 1

            elif bill == 10:  
                s[5] -= 1
                if s[5] < 0:
                    return False
                s[10] += 1

            else:
                s[5] += 1
        return True