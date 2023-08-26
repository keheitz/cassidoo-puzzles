from explode_string import explode_string

def test_explode_string_with_whitespace():
    """Test explode_string removes whitespace characters"""
    exploded = explode_string('Ahh, abracadabra!')
    assert exploded == ['!',',','A','aaaaa','bb','c','d','hh','rr']

def test_explode_on_raw_string():
    """Test explode_string on string with no alphabet or numeric characters"""
    exploded = explode_string(r'\o/\o/')
    assert exploded == ['//',r'\\','oo']
