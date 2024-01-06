class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // init dp[i] = 1 for 0 <= i < n
        // if nums[i] > nums[j]:
        //     dp[i] = max(dp[i], 1 + dp[j])
        // for   0 <= i < n and 0 <= j < i
        // nums: 1,6,2,3,1
        // dp:   1,2,2,3,1      
        // max(dp) = 3
        size_t n = nums.size();
        vector<int> dp; 

        for (int i = 0; i < n; i++) {
            dp.push_back(1);
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        int _mx = 0;
        for (auto it = dp.begin(); it != dp.end(); it++)
            _mx = max(_mx, *it);
        return _mx;
        
    }
};
