from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        result = []
        traces = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        trie  = {}
        def insert(word):
            t = trie
            for w in word:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t["#"] = word
        
        for word in words:
            insert(word)


        def search(i, j, node):
            ch = board[i][j]
            if ch not in node:
                return

            nxt_node = node[ch]
            if "#" in nxt_node:
                result.append(nxt_node["#"])
                del nxt_node["#"] 
        
            board[i][j] = "#"
            for x, y in traces:
                xi, yj = x + i, y + j
                if 0 <= xi < m and 0 <= yj < n and board[xi][yj] != "#":
                    search(xi, yj, nxt_node)
            
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                search(i, j, trie)

        return result