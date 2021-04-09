class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.lookup:
            # [# of occurrences, position in values]
            self.lookup[val] = [1, len(self.values)]
            self.values.append(val)
            return True
        else:
            self.lookup[val][0] += 1
            self.values.append(val)
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.lookup:
            self.lookup[val][0] -= 1
            
            self.values.remove(val)
            if self.lookup[val][0] == 0:
                # clear it from the lookup and values list
                self.lookup.pop(val)     
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.sample(self.values, 1)[0]
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()