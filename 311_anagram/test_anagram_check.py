"""Tests for checking if one string is an anagram of another"""
from anagram_check import is_anagram

def test_is_anagram_true():
    """Test two strings that are an anagram of one another"""
    assert is_anagram("race", "care")

def test_is_anagram_false():
    """Test two strings that are not an anagram of one another'"""
    assert not is_anagram("barbie", "oppenheimer")
