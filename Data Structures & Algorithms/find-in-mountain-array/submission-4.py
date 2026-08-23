class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        if mountainArr.length() < 2:
            return -1
            
        cache = {}

        # Cached Getter
        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        left, right = 0, mountainArr.length() - 1
    
        while left < right:
            mid = left + (right - left) // 2

            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        def evaluateMountain(left, right, hill):
            while left <= right:
                mid = left + (right - left) // 2
                value = get(mid)

                if value == target:
                    return mid

                if hill:
                    if value < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                        
                else:
                    if value < target:
                        right = mid - 1
                    else: 
                        left = mid + 1

            return -1

         ## Ascend to mountain
        idx = evaluateMountain(0, peak, True)
        if idx != -1:
            return idx
        
        ## Descend to mountain
        return evaluateMountain(peak + 1, mountainArr.length() - 1, False)    