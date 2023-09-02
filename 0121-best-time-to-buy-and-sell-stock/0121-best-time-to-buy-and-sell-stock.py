class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        min_price = sys.maxsize

        for p in prices:
            min_price = min(min_price, p)
            benefit = max(benefit, p-min_price)
        
        return benefit