class Solution {
public:
    vector<string> fizzBuzz(int n) {
        // multiples of 3 output Fizz
        // multiples of 5 output Buzz
        // multiples of both 3 and 5 output Buzz
        vector<string> result;
        for (int i = 1; i <= n; ++i)
        {
            string s = to_string(i);
            if (i % 3 == 0) {
                s = "Fizz";
            }
            if (i % 5 == 0) {
                if (s == "Fizz")
                    s.append("Buzz");
                else
                    s = "Buzz";
            }
            result.push_back(s);
        }
        return result;
    }
};