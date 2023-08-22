"""Module to find maximum profit from an ordered schedule of prices"""
def find_maximum_profit(price_schedule):
    """Returns highest profit for single buy/sell within ordered list"""
    profit = 0
    for index,price in enumerate(price_schedule):
        sale_vals = price_schedule[ index+1 : len(price_schedule) ]
        if sale_vals:
            potential_profits = [x - price for x in sale_vals]
            greatest_profit = max(potential_profits)
            if greatest_profit > profit:
                profit = greatest_profit
    return profit
