class Solution {
public:
    std::string int_to_string(int num) {
        std::ostringstream temp;
        temp << num;
        return temp.str();
    
    }
    
    std::vector<std::string> fizzBuzz(int n) {
        std::vector<std::string> result;
        for (int i=1;i<=n;i++) {
            if (i % 3 == 0 && i % 5 != 0) {
                result.push_back("Fizz");
            }
            else if (i % 5 == 0 && i % 3 != 0) {
                result.push_back("Buzz");
            }
            else if (i % 5 == 0 && i % 3 == 0) {
                result.push_back("FizzBuzz");
            }
            else {
            result.push_back(int_to_string(i));
            }
        }
        return result;
    }
};