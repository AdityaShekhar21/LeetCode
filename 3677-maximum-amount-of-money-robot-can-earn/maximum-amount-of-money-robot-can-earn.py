class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] → max coins at (i,j) using k neutralizations
        dp = [[[-10**15]*3 for _ in range(n)] for _ in range(m)]
        
        # start
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0  # use neutralization
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -10**15:
                        continue
                    
                    for di, dj in [(1,0), (0,1)]:
                        ni, nj = i+di, j+dj
                        if ni >= m or nj >= n:
                            continue
                        
                        val = coins[ni][nj]
                        
                        # normal move
                        dp[ni][nj][k] = max(
                            dp[ni][nj][k],
                            dp[i][j][k] + val
                        )
                        
                        # use neutralization if negative
                        if val < 0 and k < 2:
                            dp[ni][nj][k+1] = max(
                                dp[ni][nj][k+1],
                                dp[i][j][k]
                            )
        
        return max(dp[m-1][n-1]) 