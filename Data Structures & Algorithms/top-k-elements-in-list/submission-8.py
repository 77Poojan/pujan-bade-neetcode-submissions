from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        counts = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashMap[num] += 1

        for key, frequency in hashMap.items():
            counts[frequency].append(key)
        
        res = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                if len(res) >= k:
                    return res
                res.append(num)
                
        return res