from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxx = max(c.values())
        maxx_counts = sum(1 for v in c.values() if v == maxx) 
        return max(len(tasks), (maxx - 1) * (n + 1) + maxx_counts)

# len(tasks) CASE
# tasks = ["A","A","A","B","B","B","C","D","E"]
# n = 2