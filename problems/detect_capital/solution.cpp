class Solution {

public:
    bool detectCapitalUse(std::string word) {
        int count = 0;
        std::string::iterator it = word.begin();
        while (it != word.end()) {
            if (std::isupper(*it)) {
                count++;
            }
            it++;
        }
        if (count == word.length()) {
            return true;
        }
        if (count == 1 && std::isupper(word[0])) {
            return true;
        }
        if (count == 0) {
            return true;
        }
        return false;
    }
};

