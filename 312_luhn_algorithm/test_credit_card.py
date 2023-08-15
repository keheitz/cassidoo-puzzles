"""Tests for cassidoo challenge 312 - luhn algorithm"""
from credit_card import CreditCard

def test_luhn_check_false():
    """Test luhn_check on invalid credit card number"""
    assert not CreditCard(123456789).luhn_check()

def test_luhn_check_true():
    """Test luhn_check on valid credit card number"""
    assert CreditCard(5555555555554444).luhn_check()

def test_card_type():
    """Check that credit card type method returns correct brand"""
    assert CreditCard(5555555555554444).card_type() == "mastercard"
