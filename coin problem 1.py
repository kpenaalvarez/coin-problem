# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:03:06 2023

@author:  Kpenaalvarez
"""

ways = 0  # Initialize the count of ways to make change

for quarters in range(5):  # 0 to 4 quarters
    remaining_amount = 100 - 25 * quarters
    for dimes in range(11):  # 0 to 10 dimes
        remaining_amount -= 10 * dimes
        for nickels in range(21):  # 0 to 20 nickels
            remaining_amount -= 5 * nickels
            pennies = remaining_amount  # Pennies fill the remaining amount
            if pennies >= 0:  # Valid combination
                ways += 1
            remaining_amount += 5 * nickels  # Reset the remaining amount
        remaining_amount += 10 * dimes  # Reset the remaining amount
    remaining_amount += 25 * quarters  # Reset the remaining amount

print(f"Total ways to make change for a dollar is {ways}")
