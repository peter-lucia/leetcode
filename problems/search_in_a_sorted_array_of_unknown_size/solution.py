# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def binary_search(self, reader, low, high, target):
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if reader.get(mid) > target:
                high = mid - 1
            elif reader.get(mid) < target:
                low = mid + 1
            else:
                return mid
        return -1
    
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low = 0
        high = 1
        while reader.get(high) < target:
            new_size = 2*(high - low)
            low = high + 1
            high = low + new_size
        return self.binary_search(reader, low, high, target)