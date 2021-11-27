class MyHashMap:

    def __init__(self):
        self.size = 2069  # large prime
        self.keys = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        key_hash = self.hash(key)
        found = False
        for i, kv in enumerate(self.keys[key_hash]):
            if kv[0] == key:
                found = True
                self.keys[key_hash][i] = (key, value)
        if not found:
            self.keys[key_hash].append((key, value))

    def get(self, key: int) -> int:
        key_hash = self.hash(key)
        for i, kv in enumerate(self.keys[key_hash]):
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        key_hash = self.hash(key)
        for i, kv in enumerate(self.keys[key_hash]):
            if kv[0] == key:
                self.keys[key_hash].pop(i)
        
    def hash(self, key: int) -> int:
        """
        Computes the hash of a string
        :param key: A string to hash
        :return: an index between 0 and hash_table_size
        """
        s = 0
        for c in str(key):
            # ord converts a string to an int
            s += ord(c)
        return s % self.size