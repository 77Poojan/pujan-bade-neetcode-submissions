from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity =  capacity
        self.cache = defaultdict()
        self.frequency = defaultdict(OrderedDict)
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        if not key in self.cache:
            return - 1

        value, count = self.cache[key]
        del self.frequency[count][key]

        if not self.frequency[count]:
            del self.frequency[count]
            if  self.min_freq == count:
                self.min_freq += 1

        self.cache[key] = (value, count + 1)
        self.frequency[count + 1][key] = None

        return value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)
            return 

        if len(self.cache) == self.capacity:
            k, _ = self.frequency[self.min_freq].popitem(last=False)
            del self.cache[k]

        if not self.frequency[self.min_freq]:
            del self.frequency[self.min_freq]
          
        self.cache[key] = (value, 1)
        self.frequency[1][key] = None
        self.min_freq = 1
        return


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)