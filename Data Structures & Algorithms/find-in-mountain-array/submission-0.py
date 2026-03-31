class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        t = mountainArr.length() - 1
        l, r = 0, t
        
        while l < r:
            mid = (l + r) // 2
            
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        
        peak = l

        def minimumIndex(l, r, hill):
            while l <= r:
                mid = (l + r) // 2
                mid_val = mountainArr.get(mid)

                if mid_val == target:
                    return mid

                if hill:
                    if mid_val < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if mid_val < target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1

        idx = minimumIndex(0, l, True)
        if idx != -1:
            return idx

        return minimumIndex(l + 1, t, False)
  