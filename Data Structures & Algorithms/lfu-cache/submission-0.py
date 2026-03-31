from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if not key in self.key_map:
            return -1
        
        value, count = self.key_map[key]

        del self.freq_map[count][key]

        if not self.freq_map[count]:
            del self.freq_map[count]
            if  self.min_freq == count:
                self.min_freq += 1
        
        self.key_map[key] = (value, count + 1)
        self.freq_map[count + 1][key] = None

        return value


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_map:
            self.key_map[key] = (value, self.key_map[key][1])
            self.get(key)
            return 

        if len(self.key_map) == self.capacity:
            k, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[k]

            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]
          
        self.key_map[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)