class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astro in asteroids:
            while stack and astro < 0 and stack[-1] > 0:
                diff = astro + stack[-1]

                if diff < 0:
                    stack.pop()

                elif diff > 0:
                    astro = 0

                else:
                    astro = 0
                    stack.pop()

            if astro:
                stack.append(astro)
        return stack
