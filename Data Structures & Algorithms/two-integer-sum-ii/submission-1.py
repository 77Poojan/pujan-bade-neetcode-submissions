class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i <= j:
            t = numbers[i] + numbers[j]
            if target == t:
                return [i + 1, j + 1]
            
            if t < target:
                i += 1
            else:
                j -= 1
        return []



