class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, p in flights:
            graph[u].append((v, p))

        heap = [(0, src, 0)]
    
        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops <= k:
                for nei, price in graph[node]:
                    heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1