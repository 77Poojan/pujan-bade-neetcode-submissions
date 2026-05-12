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
                for child_key, child_node in node.items():
                    if child_key != "#" and dfs(i + 1, child_node):
                        return True
                return False

            if ch not in node:
                return False
    
            return dfs(i + 1, node[ch]) 

        return dfs(0, self.trie)