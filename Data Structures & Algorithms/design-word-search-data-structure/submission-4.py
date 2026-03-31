class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t["#"] = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return "#" in node
            
            ch = word[i]
            if ch == ".":
                for k in node:
                    if k != "#" and dfs(i + 1, node[k]):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(i + 1, node[ch])

        return dfs(0, self.trie)