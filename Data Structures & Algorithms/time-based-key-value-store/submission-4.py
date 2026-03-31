from bisect import bisect_right

class TimeMap:

    
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        idx = bisect_right(values, (timestamp, chr(127))) - 1

        if idx >= 0:
            return values[idx][1]
        return ""
