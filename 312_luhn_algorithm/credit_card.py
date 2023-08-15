"""Luhn algorithm credit card check"""

class CreditCard:
    """Class representing a credit card"""

    def __init__(self, card_number):
        self.card_number = card_number

    def luhn_check(self):
        """Check if card number is valid under luhn algorithm"""
        return False

    def card_type(self):
        """Returns the card type - visa, mastercard, or discover"""
        return 'visa'
