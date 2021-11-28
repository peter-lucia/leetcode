from bisect import bisect_right
class TimeMap:

    # approach #1

    # use a hashmap
    # key: [(timestamp, value), (timestamp, value)]

    # approach #2

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp increases with each successive call,
        # so we can just append and they will be sorted
        # by timestamp in increasing order

        # create two defaultdicts for timestamps and values

        # we could use one lookup with a list of tuples
        # where lookup[key] = [(timestamp, value), (timestamp1, value1)]
        # but bisect only provides the key parameter in python 3.10+

        self.lookup[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if self.lookup.get(key) is None:
            return ""

        # If the last (and greatest) timestamp for this key is smaller
        # than the timestamp requested, return the last timestamp
        if self.lookup[key][-1][0] < timestamp:
            return self.lookup[key][-1][1]
        
        low = 0
        high = len(self.lookup[key]) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.lookup[key][mid][0] < timestamp:
                low = mid + 1
            elif self.lookup[key][mid][0] > timestamp:
                high = mid - 1
            else:
                # found it, return the value
                return self.lookup[key][mid][1]
        # since low is 0, no values <= timestamp exist in the array for this key
        if low == 0:
            return ""
        # the exact timestamp was not found, but since we completed binary search
        # we know that all values < low are <= the desired timestamp, 
        # so we return the value just to the left of low
        return self.lookup[key][low-1][1]  # all values <= to timestamp are to the left of low

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)