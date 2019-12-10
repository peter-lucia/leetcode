class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> lookup;
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i) {
            int needed_num = target - nums[i];
            if (lookup.count(needed_num) > 0) {
                result.push_back(lookup[needed_num]);
                result.push_back(i);
                return result;
            }
            lookup.insert(pair(nums[i], i));
        }
        return result;
    }
};