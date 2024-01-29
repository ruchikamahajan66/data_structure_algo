"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


def maxProfit_approach1(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maximum_profit_so_far = float('-inf')
    for i in range(0, len(prices)):
        for j in range(1, len(prices)):
                if prices[i] < prices[j] and i < j:
                    maximum_profit = abs(prices[i] - prices[j])
                    if maximum_profit > maximum_profit_so_far:
                        maximum_profit_so_far = maximum_profit
    if maximum_profit_so_far == float('-inf'):
        return 0
    else:
        return maximum_profit_so_far


def maxProfit_approach2(prices):
    buy = prices[0]
    maximum_profit = 0
    for i in range(1, len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        elif prices[i] - buy > maximum_profit:
            maximum_profit = prices[i] - buy
    return maximum_profit





if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7,6,4,3,1]
    # print(maxProfit_approach1(prices))
    print(maxProfit_approach2(prices))
