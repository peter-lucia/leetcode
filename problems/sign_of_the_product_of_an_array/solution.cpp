class Solution {
public:
    int arraySign(vector<int>& nums) {
        int num_negatives = 0;
        for (const int &num : nums) 
        {
            if (num < 0)
                ++num_negatives;
            if (num == 0)
                return 0;
        }
        if (num_negatives % 2 == 0)
            return 1;
        return -1;
            
    }
};