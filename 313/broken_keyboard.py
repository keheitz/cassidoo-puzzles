"""Module providing broken keyboard function"""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
def type_reverse_on_vowels(text):
    """Reverses prior string on vowels"""
    output = ""
    for letter in text:
        if letter in vowels:
            output = output[::-1]
        else:
            output += letter
    return output
