class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(n) = f(n-1) + f(n-2) ..... f(2) + f(1)
        # f(2) = 2
        # f(1) = 1
        # ans= 1
        # prevCase = ans
        # for i in range(1,n):#used temp here to save the previous case so that I can store in in prevCase Later
        #     temp = ans
        #     ans += prevCase
        #     prevCase = temp
            
            
            
        # return ans
        
        
        # DP verisons (Bottom Up) Tabulation
        
        if n == 1:
            return 1
        
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
            
        return dp[n]