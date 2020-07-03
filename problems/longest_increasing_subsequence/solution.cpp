class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        
        vector<int> arr(nums.size());
        arr[0] = 1;
        
        int max_ans = 1;
        
        for (int i = 1; i < arr.size(); ++i) {
            int max_val = 0;
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) {
                    max_val = std::max(max_val, arr[j]);
                }
            }
            arr[i] = max_val + 1;
            max_ans = max(max_ans, arr[i]);
        }
        return max_ans;
    }
};