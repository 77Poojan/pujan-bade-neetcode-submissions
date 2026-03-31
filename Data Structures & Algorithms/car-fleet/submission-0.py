class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = [(p, s) for p, s in zip(position, speed)]
        combo.sort(reverse=True)
        stack = []

        for p, s in combo:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)