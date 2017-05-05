class Solution {

void printVector(std::vector<int> &blah) {
    //not changing the vector, which is passed by reference.
    std::cout << "[";
    for (std::vector<int>::iterator it = blah.begin(); it != blah.end();it++) {
        std::cout << *it << ", ";
    }
    std::cout << "]\n";
    return;

}

public:
    int singleNumber(std::vector<int> &nums) {

        if (nums.size() == 1) {
            return nums[0];
        }
        //sort the integers

        std::sort(nums.begin(), nums.end());
        // printVector(nums);

        //go step by step through each one until only one is found
//        std::vector<int>::iterator it = nums.begin();
        int next = 1;
//        do {
        for (std::vector<int>::iterator it = nums.begin();it != nums.end(); it += 2) {
            int prev = *it;
            // std::cout << "prev: " << *it << "\n";
            // std::cout << "next: " << nums[next] << "\n";
            if (prev != nums[next]) {
                return prev;
            }
            next += 2;
//            it += 2;

        } //while(it != nums.end());



        return 0;
    }

};