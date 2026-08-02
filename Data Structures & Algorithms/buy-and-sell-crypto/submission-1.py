class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        if len(prices) == 1:
            return 0
        right = 1
        
        while right < len(prices) :
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right]-prices[left])
                right+=1
            elif prices[left] > prices[right]:
                left = right
                right+=1
            else:
                right+=1
            
        return max_profit