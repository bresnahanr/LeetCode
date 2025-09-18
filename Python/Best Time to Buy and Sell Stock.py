from math import inf


class Solution:

    def best_time_to_buy_and_sell_stock(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

    def best_time_to_buy_and_sell_stock2(self, prices):
        n = len(prices)
        buy_prices = inf
        profit = 0
        
        for i in range(n):
            if prices[i] < buy_prices:
                buy_prices = prices[i]
            else:
                profit += prices[i] - buy_prices
                buy_prices = prices[i]
        return profit
    
prices = [7,1,5,3,6,4]
sol = Solution()
ans1 = sol.best_time_to_buy_and_sell_stock(prices)
print(ans1)

ans2 = sol.best_time_to_buy_and_sell_stock2(prices)
print(ans2)