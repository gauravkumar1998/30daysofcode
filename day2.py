'''Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the
meal price being added as tip), and tax percent (the percentage of the meal
price being added as tax) for a meal, find and print the meal's total cost.
Print the total meal cost, where total cost is the rounded integer result of the
entire bill (meal cost with added tax and tip).

-----'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip,tax,total=0.0,0.0,0.0
    tip=meal_cost*(tip_percent/100)
    tax=meal_cost*(tax_percent/100)
    total=meal_cost+tip+tax
    return(print(round(total)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
