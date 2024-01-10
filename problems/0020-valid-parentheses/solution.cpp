class Solution {
public:
 bool isValid(string s) {
     // push each elem to stack except
     // when finding a closing bracket
     // pop stack and make sure the
     // popped bracket from the
     // stack is a match
     // count # of brackets
     // processed via mx_sz to ensure
     // all are processed
     deque<char> q;
     map<char, char> lookup = {
       {'{', '}'},
       {'(', ')'},
       {'[', ']'}
     };
     set<char> _open = {'(',
     '[', '{'};
     set<char> _close = {
       ')',
       ']',
       '}'
     };
     int mx_sz = 0;
     for (const auto &c : s){
       if (_open.contains(c)) {
         q.push_back(c);
         mx_sz++;
       } else {
         if (!q.empty()) {
           char d = q.back();
           q.pop_back();
           mx_sz++;
           if (!(_close.contains(c)
           && _open.contains(d)
           && lookup[d] == c)) {
             return false;
           }
         }
       }
     }
    
     return q.empty() 
     && mx_sz == s.length();

    
  }
};
