"""
121. Best Time to Buy and Sell Stock

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
"""


def maximum_profit(prices):
    current_day = 0
    possible_last_day = len(prices) - 2
    max_profit = 0
    transaction_logbook = {}
    while current_day < possible_last_day:
        purchased_price = prices[current_day]
        temp_max_profit = 0

        for i in range(current_day + 1, len(prices)):
            current_profit = prices[i] - purchased_price
            if current_profit <= 0:
                continue
            if current_profit > temp_max_profit:
                temp_max_profit = current_profit
                transaction_logbook[purchased_price] = i
        if temp_max_profit and temp_max_profit > max_profit:
            max_profit = temp_max_profit

        current_day += 1
    return max_profit


def main():
    cases = [
        {
            "prices": [7, 1, 5, 3, 6, 4],
            "answer": 5,
        },
        {
            "prices": [7, 6, 4, 3, 1],
            "answer": 0,

        }
    ]
    for case in cases:
        assert maximum_profit(case['prices']) == case["answer"]


if __name__ == '__main__':
    main()






































