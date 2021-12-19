class SnapshotArray:
    # Keep track of history of each element in a dictionary mapping
    # indexes to a list of snap_ids and values:
    # {
    #   0: [[0, 0], [0, 3]],
    #   1: [[0, 0], [0, 2]],
    #   2: [[0, 0]],
    #}
    

    def __init__(self, length: int):
        self.snapshots = defaultdict(list)
        for i in range(length):
            self.snapshots[i] = [[0, 0]]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append([self.snap_id, val])

    def snap(self) -> int:
        ans = self.snap_id
        self.snap_id += 1
        return ans

    def get(self, index: int, snap_id: int) -> int:
        # O(logn) - binary search
        # Get the idx of the last occurrence of the requested snap_id
        # by getting the first index where all elements are less than snap_id + 1
        # and then subracting one from that index
        idx_last_snap_id = bisect.bisect(self.snapshots[index], [snap_id + 1]) - 1
        return self.snapshots[index][idx_last_snap_id][1]
                

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)