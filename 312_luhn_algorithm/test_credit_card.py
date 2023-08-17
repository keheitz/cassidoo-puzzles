"""Tests for cassidoo challenge 312 - luhn algorithm"""
from credit_card import CreditCard

def test_luhn_check_false():
    """Test luhn_check on invalid credit card number"""
    assert not CreditCard(123456789).luhn_check_is_valid()

def test_luhn_check_true():
    """Test luhn_check on valid credit card number"""
    assert CreditCard(5555555555554444).luhn_check_is_valid()

def test_luhn_check_true_no_auth():
    """Test luhn_check on valid credit card number"""
    assert CreditCard(4000002760003184).luhn_check_is_valid()

def test_card_type_mastercard():
    """Check that credit card type method returns correct brand"""
    assert CreditCard(5555555555554444).card_type() == "mastercard"

def test_card_type_visa():
    """Check that credit card type method returns correct brand"""
    assert CreditCard(4000002760003184).card_type() == "visa"

def test_card_type_discover():
    """Check that credit card type method returns correct brand"""
    assert CreditCard(6011000998034767).card_type() == "discover"
