void printVector(vector<string> v) {
    for (int i = 0; i < v.size(); i++) {
        if (i == 0) {
            cout << "[" << v[i] << ", ";
        } else if (i == v.size() - 1) {
            cout << v[i];
        } else {
            cout << v[i] << ", ";
        }
    }
    cout << "]\n";
}

void printStringCharMap(map<string, char> m) {
    cout << "{";
    for (auto it = m.begin(); it != m.end(); it++) {
        cout << it->first << "->" << it->second << ", ";
    }
    cout << "}\n";
}

void printCharStringMap(map<char, string> m) {
    cout << "{";
    for (auto it = m.begin(); it != m.end(); it++) {
        cout << it->first << "->" << it->second << ", ";
    }
    cout << "}\n";
}

vector<string> splitString(string s, char delim) {
    size_t pos = 0;
    vector<string> tokens;

    while ((pos = s.find(delim)) != std::string::npos) {
        string token = s.substr(0, pos);
        tokens.push_back(token);
        s = s.erase(0, pos+1);
    }
    if (s.size() > 0) {
        tokens.push_back(s);
    }
    // printVector(tokens);
    return tokens;
}

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        // 1. split string into list of words with ' ' as a deliminator
        // 2. lookupWord maps a word to a pattern identifier
        // 3. lookupPattern maps a pattern character to the first word that used it
        // 4. if word already exists in lookupWord, ensure its mapped to pattern
        //    identifier generates the same pattern as is passed to this function
        // 5. if the current pattern already exists in lookupPattern, ensure its mapped to word
        //    matches the current word
        map<string, char> lookupWord;
        map<char, string> lookupPattern;
        char delim = ' ';
        vector<string> tokens = splitString(s, delim);
        if (tokens.size() != pattern.length()) {
            return false;
        }
        int pPos = 0;
        while (pPos < tokens.size() - 1) {
            string each = tokens[pPos];
            char c = pattern[pPos];
            if (lookupWord.contains(each) && lookupWord.find(each)->second != c) {
                return false;
            } else if (lookupPattern.contains(c) && lookupPattern[c] != each){
                return false;
            }
            if (!lookupWord.contains(each)) {
                lookupWord.insert({each, c});
            }
            if (!lookupPattern.contains(c)) {
                lookupPattern.insert({c, each});
            }
            pPos++;
        }

        string lastWord = tokens[pPos];
        // printCharStringMap(lookupPattern);
        // printStringCharMap(lookupWord);
        if (lookupWord.contains(lastWord) && lookupWord.find(lastWord)->second != pattern[pPos]) {
            return false;
        } else if (lookupPattern.contains(pattern[pPos]) && lookupPattern[pattern[pPos]] != lastWord) {
            return false;
        }
        return true;
    }
};
