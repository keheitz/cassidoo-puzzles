"""Module to check if one string is an anagram of the other"""
def is_anagram(first,second):
    """Returns true if s is an anagram of t"""
    if len(first) != len(second):
        return False
    return sorted(first) == sorted(second)
