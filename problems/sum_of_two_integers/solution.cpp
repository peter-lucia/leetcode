class Solution {
public:
    int getSum(int a, int b) {
        while (b !=0) {
            int carry = a & b;
            a = a ^ b; //a is now a binary representation of all numbers in either a or b but not both.
            b = carry << 1; //shift carry left by 1
        }
        return a;
    }
    
};
