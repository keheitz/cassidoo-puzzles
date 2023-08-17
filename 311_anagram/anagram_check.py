"""Module to check if one string is an anagram of the other"""
def is_anagram(s, t):
    """Returns true if s is an anagram of t"""
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
