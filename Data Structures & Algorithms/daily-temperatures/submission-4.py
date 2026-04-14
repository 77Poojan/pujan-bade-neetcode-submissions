class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        dp = [0] * n
        stack = [(0, temperatures[0])]
        prev = temperatures[0]

        for idx, temperature in enumerate(temperatures[1:]):
            idx += 1
            if prev < temperature:
                while stack:
                    i, temp = stack.pop()
                    if temp >= temperature:
                        stack.append((i, temp))
                        break
                    dp[i] = idx - i
           
            stack.append((idx, temperature))
            prev = temperature

        return dp