class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // keep track of min price
        // subtract min price from current price
        // set max profit to the that if it's greater
        if (!prices.size()) {
            return 0;
        }

        int minPrice = prices[0];
        int maxProfit = 0;

        for (const int &p : prices) {
            maxProfit = max(maxProfit, p - minPrice);
            minPrice = min(minPrice, p);
        }
        return maxProfit;
    }
};
