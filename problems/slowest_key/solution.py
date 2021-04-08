class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
               
        max_key = None
        max_diff = 0
        n = len(releaseTimes)
        for i in range(n):
            key = keysPressed[i]
            if i == 0:
                diff = releaseTimes[i]
            else:
                diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > max_diff:
                max_diff = diff
                max_key = key
            elif diff == max_diff:
                max_key = sorted([key, max_key], reverse=True)[0]
            
        return max_key
            