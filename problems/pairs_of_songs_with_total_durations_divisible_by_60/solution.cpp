#include <unordered_map>

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        unordered_map<int,int> lookup = {};
        int counter = 0;
        for (const int &t : time) {
            int num_needed = (60 + (-t % 60)) % 60;
            int curr_remainder = t % 60;
            if (lookup.find(num_needed) != lookup.end())
                counter += lookup[num_needed];
            if (lookup.find(curr_remainder) != lookup.end())
                lookup[curr_remainder] += 1;
            else
                lookup[curr_remainder] = 1;
        }
        return counter;
    }
};