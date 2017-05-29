class Solution {
public:
    char findTheDifference(std::string s, std::string t) {
        std::unordered_map<char, int> vals;
        std::unordered_map<char, int> valt;

        for (std::string::iterator it = s.begin();it < s.end();it++) {
            std::unordered_map<char, int>::iterator found = vals.find(*it);
            if (found == vals.end()) {
                //not found
                vals.insert({*it, 0});
            } else {
                found->second += 1;
            }
        }
        for (std::string::iterator it = t.begin(); it < t.end(); it++) {
            std::unordered_map<char, int>::iterator found = valt.find(*it);
            if (found == vals.end()) {
                //not found
                valt.insert({*it, 0});
            } else {
                found->second += 1;
                std::unordered_map<char, int>::iterator in_s_too = vals.find(*it);
                if (in_s_too != vals.end()) {
                    //current character is also in s
                    if (in_s_too->second < found->second) {
                        //number of occurences in s is fewer than t now.
                        return *it;
                    }
                }
            }
        }
        for (std::string::iterator it = t.begin(); it < t.end(); it++) {
            if (vals.find(*it) == vals.end()) {
                //character is not in string s
                return *it;
            }
        }

        return '0';

    }
};