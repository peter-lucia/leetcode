class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // use map<string, vector<string>>;
        // sort the letters of each word to determine key
        // append word to vector its key maps to

        map<string, vector<string>> m;

        for (const string &each : strs) {
            string key = each;
            sort(key.begin(), key.end());
            m[key].push_back(each);
        }

        vector<vector<string>> result;

        for (const pair<string, vector<string>> &p : m) {
            vector<string> t;
            for (const string &value : p.second) {
                t.push_back(value);
            }
            result.push_back(t);
        }
        return result;
        
    }
};
