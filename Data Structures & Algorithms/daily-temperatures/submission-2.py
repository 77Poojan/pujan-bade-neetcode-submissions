class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = [(temperatures[0], 0)]
        # prev = temperatures[0]
        # temp_diff = [0] * len(temperatures)
        
        # for idx, temp in enumerate(temperatures[1:]):
        #     idx += 1
        #     if temp > prev:
        #         while stack:
        #             k, v = stack.pop()
        #             if k >= temp:
        #                 stack.append((k, v))
        #                 break
        #             temp_diff[v] = idx - v

        #     stack.append((temp, idx))
        #     prev = temp 

        # return temp_diff

        stack = []  
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((t, i))

        return res


            