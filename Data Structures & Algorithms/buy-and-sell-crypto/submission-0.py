class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = prices[0]
        right = prices[1]
        i = 1
        while i < len(prices)-1:
            if left < right:
                max_profit = max(max_profit, right-left)
                right = prices[i+1]
            elif left > right:
                left = right
                right = prices[i+1]
            else:
                right = prices[i+1]
            i+=1
        return max_profit