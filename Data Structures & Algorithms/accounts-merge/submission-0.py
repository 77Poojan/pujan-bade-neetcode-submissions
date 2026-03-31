from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        emailToName = {}

        # Build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                emailToName[email] = name

        visited = set()
        res = []

        def dfs(email, comp):
            visited.add(email)
            comp.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, comp)

        # Traverse all emails
        for email in graph:
            if email not in visited:
                comp = []
                dfs(email, comp)
                res.append([emailToName[email]] + sorted(comp))

        return res