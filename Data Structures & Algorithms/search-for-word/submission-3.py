class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = 0

        def backtrack(i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or j >= n or i >= m: 
                return False

            if board[i][j] == "#" or board[i][j] != word[k]:
                return False
            
            board[i][j] = "#"

            grid = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for x, y in grid:
                r, c = x + i, y + j
                if backtrack(r, c, k + 1):
                    return True

            board[i][j] = word[k]   
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False

        
