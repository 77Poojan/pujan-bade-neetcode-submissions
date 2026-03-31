class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        
        if "0000" in dead:
            return -1

        q = deque([("0000",0)])
        visited = {"0000"}

        while q:
            state, count = q.popleft()

            if state == target:
                return count

            for i in range(4):
                digit = int(state[i])

                for j in [1, -1]:
                    new_digit = (digit + j) % 10
                    new_combo = state[:i] + str(new_digit) + state[i+1:] 

                    if new_combo not in dead and new_combo not in visited:
                        visited.add(new_combo)
                        q.append((new_combo, count + 1))
        return -1
