class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        // init
            // start_int64_terval = 0
            // end_int64_terval = 0
        // for each num
            // if last num + 1 < current num
                // end_int64_terval = i-1
                // append int64_terval
                // start_int64_terval = i
        // e.g. [0,1,2],[4,5],[7]
        // e.g. [0],[2],[4,5],[7]
        // e.g. [0],[2,3],[5],[7]
        vector<pair<int64_t, int64_t>> result;
        if (nums.size() == 0)
            return {};
        else if (nums.size() == 1)
            return {to_string(nums[0])};


        int64_t n = nums.size();
        int64_t j = 1;
        pair<int64_t, int64_t> current_interval = {nums[0], 0};
        while (j < n) {
            if (nums[j-1] + 1 < nums[j]) {
                current_interval.second = nums[j-1];
                result.push_back(current_interval);
                current_interval = pair<int64_t, int64_t>{nums[j], INT64_MAX};
            } else if (j == n-1) {
                current_interval.second = nums[j];
                result.push_back(current_interval);
            }
            j++;
        }
        if (current_interval.second == INT64_MAX) {
            result.push_back(current_interval);
        }
        // for (auto each : result) {
            // cout << each.first << ", " << each.second << "\n";
        // }

        // convert result to correct format
        // if any int64_terval pair has the same number, convert to "x" instead of "x->y"
        vector<string> ans;
        for (auto each : result) {
            if (each.first != each.second && each.second != INT64_MAX)
                ans.push_back(to_string(each.first) + "->" + to_string(each.second));
            else
                ans.push_back(to_string(each.first));
        }
        return ans;
        
    }
};
