class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [(p, s) for p, s in zip(position, speed)]
        data.sort(reverse = True)
        stack = []
        

        for p, s in data:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()
        return len(stack)

     

