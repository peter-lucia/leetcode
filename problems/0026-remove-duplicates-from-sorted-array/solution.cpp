class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // keep track of last unique number and current number
        // if last unique number != curr, increment idx_last_unique
        // and swap nums[curr] with nums[idx_last_unique]


        int n = nums.size();
        int idx_last_unique = 0;
        int idx_curr = 1;

        while (idx_curr < n) {
            if (nums[idx_last_unique] == nums[idx_curr]) {
                idx_curr++;
            } else {
                idx_last_unique++;
                nums[idx_last_unique] = nums[idx_curr];
                idx_curr++;
            }
            // cout << "[";
            // for (const int &num: nums) {
            //     cout << num << " ";
            // }
            // cout << "]\n";
            
        }
        return ++idx_last_unique;
        
    }
};
