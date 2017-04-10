class Solution {
public:
std::string reverseWords(std::string s) {
    std::string::iterator it = s.begin();
    std::string temp;
    std::string result;
    while (it != s.end()) {
        if (*it == ' ') {
            std::reverse(temp.begin(), temp.end());
            result += temp;
            result += " ";
            temp = "";
        }
        else {
            temp += *it;
        }
        it++;
    }
    //needed since it.end() will break the while loop before we can temp to the result.
    std::reverse(temp.begin(), temp.end());
    result += temp;
    return result;

}
};