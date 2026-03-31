class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            first, last = matrix[i][0], matrix[i][-1]

            if target == first or target == last:
                return True

            if first < target < last:
                left, right = 0, n - 1

                while left <= right:
                    mid = left + (right - left) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left += 1
                    else:
                        right -= 1

                return False
        return False