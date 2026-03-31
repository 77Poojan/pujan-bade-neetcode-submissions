class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # def distance(x, y):
        #     return x**2 + y**2

        # graphs = []
        # for x, y in points:
        #     d = distance(x, y)
        #     graphs.append((d, x, y))
         
        # heapq.heapify(graphs)
        # return [(x, y) for _, x, y in heapq.nsmallest(k, graphs)]

        def distance(x, y):
            return (x**2 + y**2)

        graphs = []
        for x, y in points:
            d = distance(x, y)
            heapq.heappush(graphs, (-d, x, y))
            if len(graphs) > k:
                heapq.heappop(graphs)
        
        return [[x, y] for _, x, y in graphs]