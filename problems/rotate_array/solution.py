class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Approach: (always write out approach with examples first to verify)
        nums = 1, 2, 3, 4, 5, 6, 7
        k = 4
        tgt_index = 0 + 4
        
        tmp = 5
        nums = 1, 2, 3, 4, 1, 6, 7
        tgt_index = (4 + 4) % (n - 1) = 1
        
        tmp = 2
        nums = 1, 5, 3, 4, 1, 6, 7
        tg_index = (1 + 4) % n = 5
        
        tmp = 6
        nums = 1, 5, 3, 4, 1, 2, 7
        """
        n = len(nums)
        
        start_idx = 0
        i = 0
        while i < n:
            current_idx = start_idx
            tmp = nums[current_idx]
            while True:
                next_idx = (current_idx + k) % n
                nums[next_idx], tmp = tmp, nums[next_idx]
                current_idx = next_idx
                i += 1
                if current_idx == start_idx:
                    break
            start_idx += 1
                

         
            
        
            