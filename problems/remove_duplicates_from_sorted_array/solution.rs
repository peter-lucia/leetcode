impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0;
        }
        // Assumes nums is sorted in increasing order
        let mut idx_last_unique = 0;
        let mut idx_curr = 1;
        
        while idx_curr < nums.len() {
            if (nums[idx_last_unique] == nums[idx_curr]) {
                idx_curr += 1;
            } else {
                idx_last_unique += 1;
                nums[idx_last_unique] = nums[idx_curr];
                idx_curr += 1;
            }
        }
        return (idx_last_unique+1) as i32;
    }
}