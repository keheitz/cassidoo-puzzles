"""Module to find maximum profit from an ordered schedule of prices"""
def explode_string(input_string: str):
    """Returns sorted array of non-whitespace chars in string"""
    sorted_chars = sorted(set(''.join(input_string.split())))
    print(sorted_chars)
    exploded = []
    for i in sorted_chars:
        exploded.append(i * input_string.count(i))
    return exploded
