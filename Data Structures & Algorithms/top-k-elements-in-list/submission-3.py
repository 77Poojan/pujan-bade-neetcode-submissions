from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # import heapq
        # c = Counter(nums)
        # heap, arr = [], []

        # for num, freq in c.items():
        #     heapq.heappush(heap, (-freq, num))
        
        # for _ in range(k):
        #     arr.append(heapq.heappop(heap)[1])
        
        # return arr

        n = len(nums)
        arr = [[] for _ in range(n + 1)]
        hashMap = defaultdict(int)

        for _, num in enumerate(nums):
            hashMap[num] += 1

        for key, freq in hashMap.items():
            arr[freq].append(key)
        
       
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

        