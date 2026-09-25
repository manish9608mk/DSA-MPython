# 121. Best Time to Buy and Sell Stock

'''
Link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given an array prices where prices[i] is the stock price
on the ith day.

Choose one day to buy and a different future day to sell.

Return the maximum profit.

Example:

prices = [7,1,5,3,6,4]
Output: 5

Buy at 1 and sell at 6.
Profit = 6 - 1 = 5
'''

'''
PATTERN:

Array
    +
Maximum profit
    +
Buy before sell
    ↓
Track Minimum + Maximum Difference

Think:
"What is the cheapest price I have seen so far?"

    ↓

Keep min_price
    +
Calculate current profit
    +
Keep max_profit
'''


def max_profit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit


# Test case
prices = [7, 1, 5, 3, 6, 4]

result = max_profit(prices)

print("Max Profit =", result)


'''
Output:

Max Profit = 5
'''


'''
TRACK MINIMUM TEMPLATE:

min_value = nums[0]
max_result = 0

for value in nums:

    min_value = min(min_value, value)

    result = value - min_value

    max_result = max(max_result, result)

return max_result


KEY IDEA:

At every price:

1. Keep the cheapest price seen so far.

2. Treat the current price as the selling price.

3. Calculate:

   profit = current price - minimum price

4. Keep the maximum profit.

Example:

prices = [7,1,5,3,6,4]

7 → min = 7
1 → min = 1
5 → profit = 4
3 → profit = 2
6 → profit = 5
4 → profit = 3

Maximum profit = 5


Why does this maintain buy before sell?

min_price only contains a price from the current day
or an earlier day.

So when calculating today's profit,
the buying price is always before the selling price.


COMPLEXITY:

Time  : O(n)
Space : O(1)


RECOGNITION TRICKS:

1. Need maximum profit
2. Choose one buy and one sell
3. Buy must happen before sell
4. Need maximum difference
5. For current value, need the minimum value before it

→ Think TRACK MINIMUM SO FAR


INTERVIEW THINKING:

Need maximum profit
    ↓
Profit = sell - buy
    ↓
For every selling price
    ↓
Need cheapest previous buying price
    ↓
Track minimum price
    ↓
Calculate current profit
    ↓
Track maximum profit
    ↓
O(n) time
O(1) space
'''


'''
And this becomes part of your Array pattern family.

When you later see:

Best Time to Buy and Sell Stock
Maximum Difference
Maximum Profit
Maximum Gain
Buy before Sell

You should ask:

"Can I track the minimum value seen so far?"

If yes:

        TRACK MINIMUM
              +
        CURRENT DIFFERENCE
              ↓
        MAXIMUM RESULT
'''