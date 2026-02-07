from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.size = length
        self.snaps = {}
        self.curr_change = {}    

    def set(self, index: int, val: int) -> None:
        self.curr_change[index] = val

    def snap(self) -> int:
        snap_id = len(self.snaps)
        # Edge case
        if len(self.curr_change) == 0:
            self.curr_change = self.snaps.get(snap_id-1, {})
        self.snaps[snap_id] = self.curr_change
        self.curr_change = {}
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.snaps:
            return -1
        if index >= self.size:
            return -1
        for i in range(snap_id, -1, -1):
            snap = self.snaps[i]
            if index in snap:
                return snap[index]
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)