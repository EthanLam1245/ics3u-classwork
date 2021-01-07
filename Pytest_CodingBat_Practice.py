# main.py file
def make_bricks(small: int, big: int, goal: int) -> bool:
    """Determines whether or not it is possible to make the goal by choosin from the given bricks.

    Args:
        small: Number of 1 inch bricks given.
        big: Number of 5 inch bricks given.
        goal: Length of the row of bricks that is needed in inches.

    Returns:
        True if it is possible to make the goal by choosing from the given bricks. False otherwise.
    """
    while goal > 4:
        if big <= 0:
            break
        goal -= 5
        big -= 1
    
    return small >= goal


def lone_sum(a: int, b: int, c: int) -> int:
    """Determines the sum of three different values. If they are the same, it will not be added.
    
    Args:
        a: Value a
        b: Value b
        c: Value c
        
    Returns:
        The sum of a, b, and c. However, ignore the values that are the same.
    """
    temp_list = [a, b, c]
    if a == b or a == c:
        temp_list.remove(a)
    if b == c or b == a:
        temp_list.remove(b)
    if c == a or c == b:
        temp_list.remove(c)

    return sum(temp_list)


def lucky_sum(a: int, b: int, c: int) -> int:
    """Determines the sum of three values. If there is a 13, all the numbers to the right of it, including 13 are not added.

    Args:
        a: Value a
        b: Value b
        c: Value c
    
    Returns:
        The sum of a, b, and c. However, the values 13 and the right of it are ignored.
    """
    temp_list = [a, b, c]
    i = 0
    while i < len(temp_list):
        if temp_list[i] == 13:
            temp_list = temp_list[:i]
            break
        i += 1
    return sum(temp_list)


def near_ten(num: int) -> bool:
    """Determines whether or not a given number is within 2 of a multiple of 10.

    Args:
        num: The number given.

    Returns:
        True if num is within 2 of a multiple of 10. Otherwise False.
    """
    num = num % 10
    return 0 <= num <= 2 or 8 <= num <= 9


def in1to10(n: int, outside_mode: bool) -> bool:
    """Determines which range a number lies in depending on the outside_mode condition.

    Args:
        n: A number.
        outside_mode: If the condition is active or not.
    
    Returns:
        True if outside_mode is active and n is greater than 9 or less than 2.
        True if outside_mode is inactive and n is between 1 and 10.
        Otherwise False.
    """
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

    
    
# test_main.py file
from main import make_bricks, lone_sum, lucky_sum, near_ten, in1to10


def test_make_bricks():
    assert make_bricks(3, 1, 8) == True
    assert make_bricks(3, 1, 9) == False
    assert make_bricks(3, 2, 10) == True
    assert make_bricks(3, 2, 8) == True
    assert make_bricks(3, 2, 9) == False
    assert make_bricks(6, 1, 11) == True
    assert make_bricks(6, 0, 11) == False
    assert make_bricks(1, 4, 11) == True
    assert make_bricks(0, 3, 10) == True
    assert make_bricks(1, 4, 12) == False
    assert make_bricks(3, 1, 7) == True
    assert make_bricks(1, 1, 7) == False
    assert make_bricks(2, 1, 7) == True
    assert make_bricks(7, 1, 11) == True
    assert make_bricks(7, 1, 8) == True
    assert make_bricks(7, 1, 13) == False
    assert make_bricks(43, 1, 46) == True
    assert make_bricks(40, 1, 46) == False
    assert make_bricks(40, 2, 47) == True
    assert make_bricks(40, 2, 50) == True
    assert make_bricks(40, 2, 52) == False
    assert make_bricks(22, 2, 33) == False
    assert make_bricks(0, 2, 10) == True
    assert make_bricks(1000000, 1000, 1000100) == True
    assert make_bricks(2, 1000000, 100003) == False
    assert make_bricks(20, 0, 19) == True
    assert make_bricks(20, 0, 21) == False
    assert make_bricks(20, 4, 51) == False
    assert make_bricks(20, 4, 39) == True


def test_lone_sum():
    assert lone_sum(1, 2, 3) == 6
    assert lone_sum(3, 2, 3) == 2
    assert lone_sum(3, 3, 3) == 0
    assert lone_sum(9, 2, 2) == 9
    assert lone_sum(2, 2, 9) == 9
    assert lone_sum(2, 9, 2) == 9
    assert lone_sum(2, 9, 3) == 14
    assert lone_sum(4, 2, 3) == 9
    assert lone_sum(1, 3, 1) == 3


def test_lucky_sum():
    assert lucky_sum(1, 2, 3) == 6
    assert lucky_sum(1, 2, 13) == 3
    assert lucky_sum(1, 13, 3) == 1
    assert lucky_sum(1, 13, 13) == 1
    assert lucky_sum(6, 5, 2) == 13
    assert lucky_sum(13, 2, 3) == 0
    assert lucky_sum(13, 2, 13) == 0
    assert lucky_sum(13, 13, 2) == 0
    assert lucky_sum(9, 4, 13) == 13
    assert lucky_sum(8, 13, 2) == 8
    assert lucky_sum(7, 2, 1) == 10
    assert lucky_sum(3, 3, 13) == 6


def test_near_ten():
    assert near_ten(12) == True
    assert near_ten(17) == False
    assert near_ten(19) == True
    assert near_ten(31) == True
    assert near_ten(6) == False
    assert near_ten(10) == True
    assert near_ten(11) == True
    assert near_ten(21) == True
    assert near_ten(22) == True
    assert near_ten(23) == False
    assert near_ten(54) == False
    assert near_ten(155) == False
    assert near_ten(158) == True
    assert near_ten(3) == False
    assert near_ten(1) == True


def test_in1to10():
    assert in1to10(5, False) == True
    assert in1to10(11, False) == False
    assert in1to10(11, True) == True
    assert in1to10(10, False) == True
    assert in1to10(10, True) == True
    assert in1to10(9, False) == True
    assert in1to10(9, True) == False
    assert in1to10(1, False) == True
    assert in1to10(1, True) == True
    assert in1to10(0, False) == False
    assert in1to10(0, True) == True
    assert in1to10(-1, False) == False
    assert in1to10(-1, True) == True
    assert in1to10(99, False) == False
    assert in1to10(-99, True) == True
    
