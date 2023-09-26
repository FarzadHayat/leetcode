# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# O(n) time, O(1) space
# My solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit, bot, top = 0, 0, 0
        for i in range(1, len(prices)):
            if prices[bot] > prices[i]:
                bot = i
            elif top <= bot or prices[top] < prices[i]:
                top = i
            if bot < top:
                profit = max(profit, prices[top] - prices[bot])
        return profit
    
# O(n) time, O(1) space
# NeetCode's first solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 # left=buy, right=sell
        maxProfit = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

# O(n) time, O(1) space
# NeetCode's second solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))