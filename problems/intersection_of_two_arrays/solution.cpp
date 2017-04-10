class Solution {
public:
std::vector<int> intersection(std::vector<int>& nums1, std::vector<int>& nums2) {
        //returns the values that are in both vectors
        if (nums1.size() == 0 || nums2.size() == 0) {
            return {};
        }
        std::vector<int> result;
        std::vector<bool> chars(1000); //should initialize all values to false.
        for (int i=0;i<nums1.size();i++) {
            chars[nums1[i]] = true;
        }
        for (int i=0;i<nums2.size();i++) {
            if (chars[nums2[i]] == true) {
                result.push_back(nums2[i]);
            }
        }


        std::sort(result.begin(), result.end());
        std::vector<int>::iterator last2 = std::unique(result.begin(), result.end()); 
        result.erase(last2, result.end()); 
        return result;

    }
};