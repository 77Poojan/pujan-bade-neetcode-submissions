from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        res = []

        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)

        def dfs(node):
            while graph[node]:
                nxt_node = graph[node].pop()
                dfs(nxt_node)
            res.append(node)
        
        dfs("JFK")
        return res[::-1]

        