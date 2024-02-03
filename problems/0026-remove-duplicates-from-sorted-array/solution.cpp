class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // keep track of first unique element at index, i
        // keep track of current element at index, j
        // i is always less than j;

        int i = 0;
        int j = 1;
        auto n = nums.size();
        while (j < n) {
            if (nums[i] == nums[j]) {
                j++;
            } else {
                i++;
                nums[i] = nums[j];
                j++;
            }
        }
        return i+1;
        
        
    }
};
