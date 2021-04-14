class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # put sticks into a min heap
        sticks = sticks.copy()
        heapq.heapify(sticks)
        # pop two smallest elements, add them up, add their sum to total cost
        total_cost = 0
        while sticks:
            if len(sticks) == 1:
                break
            elem1 = heapq.heappop(sticks)
            elem2 = heapq.heappop(sticks)
            new_elem = elem1 + elem2
            total_cost += new_elem
            heapq.heappush(sticks, new_elem)
            
        # return total cost
        return total_cost