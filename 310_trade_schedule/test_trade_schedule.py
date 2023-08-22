"""Tests for identifying maximum profit for an ordered price schedule"""
from trade_schedule import find_maximum_profit

def test_find_maximum_profit():
    """Given an ordered schedule with viable profit, return the profit value"""
    assert find_maximum_profit([7,1,5,3,6,4]) == 5

def test_find_maximum_profit_not_viable():
    """Given an ordered schedule without viable profit, return 0"""
    assert find_maximum_profit([7,6,5,4,3,2]) == 0
