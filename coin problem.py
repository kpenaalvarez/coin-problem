# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:22:09 2023

@author: Kpenaalvarez
"""

def count_coin_change(coins, amount):
    # Initialize a table to store the results
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make 0 cents

    # Iterate through each coin
    for coin in coins:
        # Update the table for each value
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


# Available coin denominations
coins = [1,5,10,25,50,100]

# Amount in cents ($1)
amount = 100

# Calculate the total number of ways to make $1
total_ways = count_coin_change(coins, amount)

print("Total number of ways to make $1:", total_ways)
