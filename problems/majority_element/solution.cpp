class Solution {
public:
    int majorityElement(vector<int> &nums) {
        unordered_map<int, int> lookup;

        int max_elem = nums[0];
        int max_elem_counts = 0;

        for (const int &num : nums) {
            if (lookup.find(num) != lookup.end()) {
                lookup[num] += 1;
            } else {
                lookup[num] = 1;
            }

            if (lookup[num] > max_elem_counts) {
                max_elem = num;
                max_elem_counts = lookup[num];
            }
        }
        return max_elem;
}

};