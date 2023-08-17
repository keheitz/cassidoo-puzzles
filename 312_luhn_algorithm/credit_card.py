"""Luhn algorithm credit card check"""

class CreditCard:
    """Class representing a credit card"""
    credit_card_types = {
                            '3': 'american express',
                            '4': 'visa',
                            '5': 'mastercard',
                            '6': 'discover'
                        }

    def __init__(self, card_number):
        self.card_number = card_number
        self.check_digit = card_number % 10 if card_number > 9 else 0
        self.payload = card_number // 10 if card_number > 9 else card_number

    def luhn_check_is_valid(self):
        """Check if card number is valid under luhn algorithm"""
        payload_array = list(map(int, str(self.payload)))
        payload_array.reverse() # start with last digit
        # Multiply even indexed numbers by 2, odd by 1
        multiplied_vals = [num * 2 for i, num in enumerate(payload_array) if not i % 2] + [
            num for i, num in enumerate(payload_array) if i % 2
        ]
        multiplier_sum = 0
        # Add the multiplied value to sum if it's single digit (less than 10),
        # otherwise get and add each digit individually
        for val in multiplied_vals:
            if val < 10:
                multiplier_sum += val
            else:
                multiplier_sum += (val % 10)
                multiplier_sum += (val // 10)
        return (10 - multiplier_sum % 10) == self.check_digit

    def card_type(self):
        """Returns the card type - visa, mastercard, or discover"""
        first_digit = str(self.card_number)[0]
        return self.credit_card_types[first_digit]
