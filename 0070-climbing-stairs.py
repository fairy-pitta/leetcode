class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [(0) for _ in range(n+1)]
        dp[0] = 1 
        for i in range(1, n+1):
            if i-1 >= 0:
                dp[i] += dp[i-1] 
            if i-2 >= 0:
                dp[i] += dp[i-2] 
        
        return dp[-1]

        