class Solution {
public:
    int row(const char n) {
        std::array<char, 10> row1 = {'q','w','e','r','t','y','u','i','o','p'};
        std::array<char, 9> row2 = {'a','s','d','f','g','h','j','k','l'};
        std::array<char, 7> row3 = {'z','x','c','v','b','n','m'};
    
        std::array<char, row1.size()>::iterator it_1 = std::find(row1.begin(), row1.end(), n);
        if (it_1 != row1.end()){
            //element 'n' found in row1
            //std::cout << n << " is in row1.\n";
            return 1;
        }
        std::array<char, row2.size()>::iterator it_2 = std::find(row2.begin(), row2.end(), n);
    
        if (it_2 != row2.end()) {
            //element 'n' found in row2
            //std::cout << n << " is in row2.\n";
            return 2;
        }
        std::array<char, row3.size()>::iterator it_3 = std::find(row3.begin(), row3.end(), n);
    
        if (it_3 != row3.end()) {
            //element 'n' found in row3
            //std::cout << n << " is in row3.\n";
            return 3;
        }

        return 0;
    }
    bool run(const std::string word) {
        bool out = true;
        int prev = row(word[0]);
        for (int i=0;i<word.length()-1;i++) {
            char next_char = word[i+1];
            int next_char_row = row(word[i+1]);
            char prev_char = word[i];
            int prev_char_row = row(word[i]);
            if (prev != row(word[i+1])){
                out = false;
                break;
            }
            else {
                prev = row(word[i]);
            }
        }
        return out;
    
    }

    std::string word_tolower(const std::string word) {
        std::string result;
        for (int i=0;i<word.length();i++) {
            if (word.at(i) <= 90 && word.at(i) >= 65) {
                result += char(word.at(i) + 32);
            }
            else {
                result += word[i];
            }
        }
        return result;
    }
    
    std::vector<std::string> words_tolower(const std::vector<std::string> words) {
        std::vector<std::string> result;
        for (int i=0;i<words.size();i++) {
            result.push_back(word_tolower(words.at(i)));
        }
        return result;
    }



    std::vector<std::string> findWords(std::vector<std::string> const &words) {
        std::vector<std::string> words_lowered = words_tolower(words);
        std::vector<std::string> result;
        for (int i=0;i<words_lowered.size();i++) {
            if (run(words_lowered.at(i))) {
                result.push_back(words.at(i));
            }
    
        }
        return result;
    }
};