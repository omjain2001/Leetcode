class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            if self.hashmap[key][-1][1] == value:
                self.hashmap[key][-1][0] = timestamp
            else:
                self.hashmap[key].append([timestamp, value])
        else:
            self.hashmap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        arr = self.hashmap[key]
        i = 0
        while i < len(arr) and arr[i][0] <= timestamp:
            i += 1
        
        i -= 1
        if i < 0:
            return ""
        return arr[i][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)