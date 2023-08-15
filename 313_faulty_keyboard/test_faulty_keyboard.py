"""Tests for cassidoo challenge 313 - faulty keyboard reversing string on vowels"""
from faulty_keyboard import type_reverse_on_vowels

def test_type_reverse_on_vowels_string():
    """Test type_reverse_on_vowels on 'string'"""
    assert type_reverse_on_vowels("string") == "rtsng"

def test_type_reverse_on_vowels_hello_world():
    """Test type_reverse_on_vowels on 'hello world!'"""
    assert type_reverse_on_vowels("hello world!") == "w hllrld!"
