class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

    # def __init__(self, capacity: int):
    #     self.LRU = []
    #     self.capacity = capacity

    # def get(self, key: int) -> int:
    #     LRU = self.LRU
    #     for l in range(len(LRU)):
    #         k, v = LRU[l]
    #         if k == key:
    #             tmp = self.LRU.pop(l)
    #             self.LRU.append(tmp)
    #             return tmp[1]
    #     return -1

    # def put(self, key: int, value: int) -> None:
    #     for i in range(len(self.LRU)):
    #         if self.LRU[i][0] == key:
    #             tmp = self.LRU.pop(i)
    #             tmp[1] = value
    #             self.LRU.append(tmp)
    #             return

    #     if len(self.LRU) >= self.capacity:
    #         self.LRU.pop(0)
    #     self.LRU.append((key, value))
        