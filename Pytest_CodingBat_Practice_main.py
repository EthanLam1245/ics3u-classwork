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
