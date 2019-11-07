class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i)
        {
            int diff = target - nums.at(i);
            for (int j = 0; j < nums.size(); ++j)
            {
                if ((nums.at(j) == diff) && (i != j))
                {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return result;
    }
};