class Solution:

    def best_time_to_buy_and_sell_stock(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
    
prices = [7,1,5,3,6,4]
sol = Solution()
ans = sol.best_time_to_buy_and_sell_stock(prices)
print(ans)