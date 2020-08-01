class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom up solution using dynamic programming
        Only the value of the coin matters
        """
        if len(coins) == 0 or amount == 0:
            return 0
        
        """
        K stores the number of coins needed to produce
            amounts ranging from 0 to the provided amount.
            Assume inf coins are required for all amounts initially
        """
        K = [float("inf") for _ in range(amount+1)]
        
        """
        Initially, to produce an amount of 0, we need 0 coins.
        """
        K[0] = 0
        
        for coin in coins:
            
            """
            Effectively skips coins larger than the amount,
            but iterates over all values from that of the coin
            up to the amount needed.
            """
            for i in range(coin, amount+1):
                """
                Since we want the fewest number of coins, take
                the minimum of the following two quantities:
                
                K[i] 
                    existing number of coins needed to create the
                    specified amount
                K[i - coin] + 1 
                    number of coins needed for the current amount,
                    but excluding the current coin 
                """
                K[i] = min(K[i], K[i - coin] + 1)
                
        """
        If we can make the desired amount, return the number
        of coins needed to produce it
        """
        if K[amount] != float("inf"):
            return K[amount]
        
        """
        We cannot produce the desired amount with any number of these coins.
        """
        return -1
            
        