from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if not self.cache.get(key, False):
            return -1
        
        # end is the front of the cache
        self.cache.move_to_end(key)
        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)