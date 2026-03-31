class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # m, n = len(matrix), len(matrix[0])
        # o = n - 1
        # nn = [[0] * (n) for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         nn[j][o - i] = matrix[i][j]
        # matrix[:] = nn


        n = len(matrix)

        # transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for row in matrix:
            row.reverse()