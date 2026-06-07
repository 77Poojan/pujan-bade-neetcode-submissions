class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        traces = [(0,1),(0,-1),(1,0),(-1,0)]

        def capture(i, j):
            board[i][j] = "T"
            for x, y in traces:
                xi, yj = x + i, y + j
                if 0 <= xi < m and 0 <= yj < n and board[xi][yj] == "O":
                    capture(xi, yj)
            return

        # Capture
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i in [0, m - 1] or j in [0, n - 1]):
                    capture(i, j)

        # Convert
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Revert
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"