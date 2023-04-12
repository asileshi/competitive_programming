class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i,amnt):
            if i>=len(coins) or amnt>amount:
                return 0
            if amnt == amount:
                return 1
            if ((i,amnt)) not in memo:
                memo[(i,amnt)] = dp(i,amnt+coins[i])+dp(i+1,amnt)
            return memo[(i,amnt)]
        return dp(0,0)