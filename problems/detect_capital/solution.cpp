class Solution {
public:
    bool detectCapitalUse(string word) {
        int n = word.length();
        
        int capital_count = 0;
        bool first_word_capital = false;
        int i = 0;
        for (const char &c : word) {
            if (c == toupper(c) ) {
                capital_count++;
                if (i == 0) {
                    first_word_capital = true;
                }
            }
            i++;
        }
        
        return capital_count == 0 || capital_count == n || (first_word_capital && capital_count == 1);
        
    }
};