class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        heapq.heapify(self.max_heap)
        self.min_heap = []
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        # TODO: Write your code here
        if len(self.max_heap) > 0 and num >= -self.max_heap[0]:
            # insert larger nums into min heap
            heapq.heappush(self.min_heap, num)

        elif len(self.min_heap) > 0 and num <= self.min_heap[0]:
            # insert smaller nums into max heap
            heapq.heappush(self.max_heap, -num)
        else:
            # no numbers yet -> num is larger than null numbers
            # so we insert larger nums into min heap
            heapq.heappush(self.min_heap, num)

        # ensure neither heap has 1 more element than the other
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()