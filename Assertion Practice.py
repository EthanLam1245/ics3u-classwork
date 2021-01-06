# Codingbat tests to assert statements

def test_string_times():
    assert string_times('Hi', 2) == 'HiHi'
    assert string_times('Hi', 3) == 'HiHiHi'
    assert string_times('Hi', 1) == 'Hi'
    assert string_times('Hi', 0) == ''
    assert string_times('Hi', 5) == 'HiHiHiHiHi'
    assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
    assert string_times('x', 4) == 'xxxx'
    assert string_times('', 4) == ''
    assert string_times('code', 2) == 'codecode'
    assert string_times('code', 3) == 'codecodecode'


def test_front_times():
    assert front_times('Chocolate', 2) == 'ChoCho'
    assert front_times('Chocolate', 3) == 'ChoChoCho'
    assert front_times('Abc', 3) == 'AbcAbcAbc'
    assert front_times('Ab', 4) == 'AbAbAbAb'
    assert front_times('A', 4) == 'AAAA'
    assert front_times('', 4) == ''
    assert front_times('Abc', 0) == ''


def test_array_front9():
    assert array_front9([1, 2, 9, 3, 4]) == True
    assert array_front9([1, 2, 3, 4, 9]) == False
    assert array_front9([1, 2, 3, 4, 5]) == False
    assert array_front9([9, 2, 3]) == True
    assert array_front9([1, 9, 9]) == True
    assert array_front9([1, 2, 3]) == False
    assert array_front9([1, 9]) == True
    assert array_front9([5, 5]) == False
    assert array_front9([2]) == False
    assert array_front9([9]) == True
    assert array_front9([]) == False
    assert array_front9([3, 9, 2, 3, 3]) == True
