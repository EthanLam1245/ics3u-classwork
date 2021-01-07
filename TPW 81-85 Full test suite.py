# main.py file
import math


# CONSTANTS
base_fare = 4
variable = 0.25

first_item = 10.95
subsequent_items = 2.95

#Exercise 81: Compute the Hypotenuse
def calculate_hypotenuse(first_side: float, second_side: float) -> float:
    """Calculate the hypotenuse of a right angle triangle.

    Args:
        first_side: The shortest side of the triangle.
        second_side: The other shortest side of the triangle.
    
    Returns:
        The length of the hypotenuse.
    """
    return math.sqrt(first_side ** 2 + second_side ** 2)


#Exercise 82: Taxi Fare
def total_fare(distance_traveled: float) -> float:
    """Calculate the taxi fare.

    Args:
        distance_traveled: The distance traveled in kilometers.

    Returns:
        The cost of the fare in dollars.
    """
    return base_fare + variable * (distance_traveled * 1000 // 140)


#Exercise 83: Shipping Calculator
def shipping_charge(number_of_items: int) -> float:
    """Calculate the shipping cost.

    Args: 
        number_of_items: The number of items needed for shipping.

    Returns:
        The cost for shipping the items in dollars.
    """
    if number_of_items > 0:
        return first_item + subsequent_items * (number_of_items - 1)
    else:
        return 0


#Exercise 84: Median of Three Values
def calculate_median(num1: float, num2: float, num3: float) -> float:
    """Calculate the median of 3 numbers.

    Args:
        num1: First number
        num2: Second number
        num3: Third number
    
    Returns:
        The median of the 3 numbers.
    """
    unsorted = [num1, num2, num3]
    largest = max(unsorted)
    smallest = min(unsorted)
    unsorted.remove(largest)
    unsorted.remove(smallest)
    return unsorted[0]


#Exercise 85: Convert an Integer to its Ordinal Number
def ordinal_number(integer: int) -> str:
    """Identifies the ordinal number from 1 through 12.

    Args:
        integer: An integer between 1 and 12 (inclusive).
    
    Returns:
        The ordinal number of that integer.
    """
    english_ordinal_numbers = "first second third fourth fifth sixth seventh eight ninth tenth eleventh twelfth".split(" ")
    if 1 <= integer <= 12:
        return english_ordinal_numbers[integer - 1]
    else:
        return ""


if __name__ == "__main__":
    main()



# test_main.py file
import math
from main import calculate_hypotenuse, total_fare, shipping_charge, calculate_median, ordinal_number


def test_calculate_hypotenuse():
    assert calculate_hypotenuse(3, 4) == 5
    assert calculate_hypotenuse(4, 3) == 5
    assert calculate_hypotenuse(12, 16) == 20
    assert calculate_hypotenuse(13, 16) == 5 * math.sqrt(17)
    assert calculate_hypotenuse(1, 1) == math.sqrt(2)


def test_total_fare():
    assert total_fare(0.14) == 4.25
    assert total_fare(0.3) == 4.5
    assert total_fare(1) == 5.75
    assert total_fare(100) == 182.5
    assert total_fare(0) == 4


def test_shipping_charge():
    assert shipping_charge(1) == 10.95
    assert shipping_charge(20) == 67
    assert shipping_charge(4) == 19.8
    assert shipping_charge(0) == 0
    assert shipping_charge(103) == 311.85


def test_calculate_median():
    assert calculate_median(-1, 0, -2) == -1
    assert calculate_median(103, 123, 219) == 123
    assert calculate_median(423, -123, 186) == 186
    assert calculate_median(100, 100, 100) == 100
    assert calculate_median(26, 23, 23) == 23


def test_ordinal_number():
    assert ordinal_number(1) == "first"
    assert ordinal_number(12) == "twelfth"  
    assert ordinal_number(6) == "sixth"
    assert ordinal_number(0) == ""
    assert ordinal_number(13) == ""
