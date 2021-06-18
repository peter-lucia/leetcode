class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int count = 0;
        for (const int &val : arr)
        {
            if (val % 2 != 0) {
                ++count;
                if (count >= 3) {
                    return true;
                }
            } else 
                count = 0;
        }
        return false;
        
    }
};