class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if (arr.size() < 3)
            return false;
        
        int pos_max = -1;
        bool ramp_up = true;
        bool found_ramp_up = false;
        
        int last_val = arr[0];
        
        for (int i = 1; i < arr.size() ; ++i) {
            if (last_val < arr[i]) {
                found_ramp_up = true;
            }
            if (last_val > arr[i]) {
                ramp_up = false;
            }
            
            if (ramp_up && last_val >= arr[i]) {
                return false;
            } else if (!ramp_up && last_val <= arr[i]) {
                return false;
            }
            
            last_val = arr[i];
        }
        
        return found_ramp_up && ramp_up == false;
        
    }
};