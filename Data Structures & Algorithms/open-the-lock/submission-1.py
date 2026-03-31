from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        q = deque([("0000",0)])
        visited = {"0000"}

        while q:
            state, steps = q.popleft()

            if state == target:
                return steps

            for i in range(4):
                digit = int(state[i])

                for move in (1, -1):
                    new_digit = (digit + move) % 10
                    nxt = state[:i] + str(new_digit) + state[i+1:]

                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps+1))
        return -1
