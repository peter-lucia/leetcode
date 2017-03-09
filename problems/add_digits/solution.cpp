class Solution {
public:
    int addDigits(int num) {
    int sum = 0;
    while ((num / 10 != 0) || (num != 0)) {
        sum += num % 10;
        num = num / 10;

    }
    if (sum >= 10) {
        return addDigits(sum);
    }
    return sum;
    }
};