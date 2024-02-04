class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // sliding window
        // i, j
        // increment sum with nums[j] 
        // subtract nums[i] from sum while sum >= target and increment i
        // Time: O(n^2)
        // Space: O(1)
        int n = nums.size();
        int sm = 0;
        int min_width = INT_MAX;
        int i = 0;
        for (int j = 0; j < n; j++) {
            sm += nums[j];
            while (sm >= target) {
                min_width = min(min_width, j-i+1);
                sm -= nums[i];
                i++;
            }
        }
        if (min_width != INT_MAX)
            return min_width;
        return 0;

    }
};
