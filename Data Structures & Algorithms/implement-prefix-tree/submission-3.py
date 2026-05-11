class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        trace = self.trie
        for ch in word:
            if ch not in trace:
                trace[ch] = {}
            trace = trace[ch]      
        trace["#"] = True

        
    def search(self, word: str) -> bool:
        trace = self.trie
        for ch in word:
            if ch not in trace:
                return False
            trace = trace[ch]    
        return "#" in trace


    def startsWith(self, prefix: str) -> bool:
        trace = self.trie
        for ch in prefix:
            if ch not in trace:
                return False
            trace = trace[ch]    

        return True
    