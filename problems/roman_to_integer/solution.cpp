class Solution {
public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> legend = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        if (s.length() == 1) {
            std::cout << legend[s[0]] << std::endl;
            return legend[s[0]];
        }
        std::vector<int> values;
        for (std::string::iterator it = s.begin();it < s.end(); it++) {
            values.push_back(legend[*it]);
        }
        int sum = 0;
        for (int i = 0; i < values.size(); i++) {
            if (i != 0 && values[i-1] < values[i]) {
                sum -= values[i-1];
                sum += (values[i] - values[i-1]);

            } else {
                sum += values[i];
            }
        }
        return sum;

    }
};