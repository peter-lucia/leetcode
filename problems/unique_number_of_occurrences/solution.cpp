class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::map<int, int> vals;
        for (int i = 0; i < arr.size(); ++i) {
            if (vals.count(arr[i]) > 0) {
                vals[arr[i]] += 1;
            } else {
                vals.insert({arr[i], 1});
            }
                
        }
        
        set<int> occurrences;
        map<int, int>::iterator it;
        
        for (it = vals.begin(); it != vals.end(); ++it) {
            occurrences.insert((*it).second);
        }
        if (occurrences.size() != vals.size())
            return false;
        return true;
    }
};