from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # sort in reverse so we can pop smallest easily
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)

        res = []

        def dfs(node):
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
            res.append(node)

        dfs("JFK")
        return res[::-1]