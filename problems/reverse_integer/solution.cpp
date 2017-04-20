class Solution {
public:
    void printStack(std::stack<int> s) {
        while (!s.empty()) {
//            std::ostringstream temp;
//            temp << s.top();
            std::cout << s.top() << "\n";
            s.pop();
        }
        return;
    }
    std::string toString(int x) {
        std::ostringstream temp;
        temp << x;
        return temp.str();
    }

    int reverse(int x) {
        //std::cout << "-----------\n";
       // std::cout << "x = " << x << "\n";
        if (x < 10 && x >= 0) {
            std::cout << "Result: " << x << "\n";
            return x;
        }
//        bool pos;
//        if (x < 0) {
//            pos = false;
//        } else {
//            pos = true;
//        }
        bool pos = (x>=0) ? true:false;
//        std::cout << "Sign: " << sign << "\n";
        if (pos) {
//            std::cout << "x is positive" << "\n";
        } else {
//            std::cout << "x is negative" << "\n";
        }

        if (!pos) {// if x is negative, make it positive
            x = -1*x;
        }
        //sign is determined, x is always positive from here on, until the sign is applied @ the end.
        std::string num = toString(x);
        if (x < 0) {
            num = num.substr(1);
        }
        std::stack<int> s;
        for (int i=0;i<num.length();i++) {
            s.push(x % 10);
            x = x/10;
        }
//        printStack(s);
        std::stack<int> s_reversed;
        for (int i=0;s.size();i++) {
            s_reversed.push(s.top());
            s.pop();
        }
//        printStack(s_reversed);
        long long int result = 0; // always initialize to zero, or else a random value will be assigned!!
        for (int i=0;i<num.length();i++) {
            //std::cout << "num.length()" << num.length() << "\n";
            long long int factor = pow(10, num.length() - 1- i);
//            std::cout << "Factor: " << factor << "\n";
            long int t1 = s_reversed.top();
            //std::cout << "t1*factor: " << t1*factor << "\n";
            result += t1* factor;
            //std::cout << "Result Current: " << result << "\n";
            s_reversed.pop();
        }
        if (result > std::numeric_limits<int>::max() || result < std::numeric_limits<int>::min()) {
            //std::cout << "Result: " << 0 << "\n";
            //std::cout << "integer too large...\n";
            return 0;
        }
        int r = result;
        if (!pos) {
            r = -1*r;
        }
        //std::cout << "Result: " << r << "\n";
//        std::cout << typeid(r).name() << "\n";
//        std::cout << r + 1 << "\n";
        return r;
    }


};