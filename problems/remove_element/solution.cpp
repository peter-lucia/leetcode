class Solution {
public:
    int removeElement(std::vector<int> &nums, int val) {

        int len = nums.size();
        if (len == 0) {

            return 0;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == val) {
                len -= 1;
                nums.erase(nums.begin() + i);
                return removeElement(nums, val);
            }

        }
        std::cout << "new length: " << len << "\n";
        return len;

    }
    void printVec(std::vector<int> &vec) {
        std::cout << "[";
        for (int i=0;i < vec.size() ; i++) { //for each value in vector vec
        }
    }

};