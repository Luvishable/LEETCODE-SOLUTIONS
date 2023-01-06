"""
1833. Maximum Ice Cream Bars
Medium

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n,
where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend,
and he wants to buy as many ice cream bars as possible.

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
"""


def max_ice_cream(costs, coins):

    sorted_costs = sorted(costs)
    price_to_pay = 0

    for i in range(len(sorted_costs)):
        if sorted_costs[i] > coins:
            return 0
        else:
            price_to_pay += sorted_costs[i]
            if price_to_pay > coins:
                return len(sorted_costs[:i])
    return len(sorted_costs)

def main():
    cases = [
        {
            "costs": [1, 3, 2, 4, 1],
            "coins": 7,
            "answer": 4
        },
        {
            "costs": [10, 6, 8, 7, 7, 8],
            "coins": 5,
            "answer": 0
        },
        {
            "costs": [1, 6, 3, 1, 2, 5],
            "coins": 20,
            "answer": 6
        }
    ]
    for case in cases:
        assert max_ice_cream(case['costs'], case["coins"]) == case["answer"]


if __name__ == '__main__':
    main()






























