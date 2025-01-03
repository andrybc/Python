class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]

        profit = 0
        
        
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i]- min_price > profit:
                profit = prices[i]- min_price
                
        
        return profit