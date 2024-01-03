class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Use the mergesort operation
        // provision an empty array where the sorted values are merged
        // assign the values of that array to nums1

        // copies values into new vector tmp
        vector<int> tmp;

        int i = 0;
        int j = 0;
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                tmp.push_back(nums1[i]);
                i++;
            } else {
                tmp.push_back(nums2[j]);
                j++;
            }
        }

        // here at most only i < nums1.size() or j < nums2.size()
        while (i < m) {
            tmp.push_back(nums1[i]);
            i++;
        }

        while (j < n) {
            tmp.push_back(nums2[j]);
            j++;
        }
        nums1 = tmp;
        
    }
};
