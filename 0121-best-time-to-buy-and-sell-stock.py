class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [(0) for _ in range(len(prices))]
        min_price = 10**7

        for i in range(len(prices)):
            dp[i] = max(dp[i], prices[i]-min_price)
            min_price = min(min_price, prices[i])
        
        return max(dp)