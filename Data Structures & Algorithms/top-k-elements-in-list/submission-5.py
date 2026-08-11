class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        hashMap = defaultdict(int)
        arr = [[] for _ in range(len(nums) + 1)] 

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

        

        
        

            

        


        




