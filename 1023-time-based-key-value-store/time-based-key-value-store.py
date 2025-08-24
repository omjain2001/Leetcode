class TimeMap:

    def __init__(self):
        self.hashmap = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[(key, timestamp)] = value
        if key in self.timestamps:
            self.timestamps[key].append(timestamp)
        else:
            self.timestamps[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        ts = self.timestamps[key]
        l = 0
        r = len(ts)-1
        while(l <= r):
            mid = (l+r)//2
            if ts[mid] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        idx = l - 1
        if idx < 0:
            return ""
        else:
            return self.hashmap[(key, ts[idx])]
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)