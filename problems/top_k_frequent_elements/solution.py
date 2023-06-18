class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      d = defaultdict(int)
      for n in nums:
        d[n] += 1
      
      # (key, count) -> (-count, key)
      # negative count to make heap
      # put the largest element at the top instead of the smallest
      vals = [(-v, k) for k, v in list(d.items())]
      heapify(vals)
      result = []
      for i in range(k):
        _, k = heappop(vals)
        result.append(k)
      return result

      
        



        