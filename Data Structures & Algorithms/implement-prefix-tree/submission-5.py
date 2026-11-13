class PrefixTree:

    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        trace = self.trie
        for w in word:
            if w not in trace:
                trace[w] = {}  
            trace = trace[w]
        trace["#"] = True


    def search(self, word: str) -> bool:
        trace = self.trie
        for w in word:
            if w not in trace:
                return False
            trace = trace[w]
        return "#" in trace
        

    def startsWith(self, prefix: str) -> bool:
        trace = self.trie
        for w in prefix:
            if w not in trace:
                return False 
            trace = trace[w]
        return True
        