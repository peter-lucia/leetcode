class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // append nums[n - k + i] for 0 <= i < k to new array
        // append nums[i] for 0 <= i < n-k to new array
        // copy the new array over into nums
        // O(n) space complexity
        // O(n) time complexity
        int n = nums.size();
        k = k % n;

        vector<int> tmp;

       
        for (int i = 0; i < k; i++) {
            tmp.push_back(nums[n-k+i]);
        }
        for (int i = 0; i < n-k; i++) {
            tmp.push_back(nums[i]);
        }
        nums = tmp;
    }
};
