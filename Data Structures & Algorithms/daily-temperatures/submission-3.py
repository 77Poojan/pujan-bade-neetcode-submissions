class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        res = [0] * (len(temperatures))
  

        for idx in range(1, len(temperatures)):
            temp = temperatures[idx]
            while stack and stack[-1][1] < temp:
                i, t = stack.pop()
                if t < temp:
                    res[i] = idx - i
            stack.append((idx, temp))
        return res