import math


# CONSTANTS
base_fare = 4
variable = 0.25

first_item = 10.95
subsequent_items = 2.95

# MAIN FUNCTION
def main():
    side_1 = get_positive_number("Please enter the first shortest side: ")
    side_2 = get_positive_number("Please enter the second shortest side: ")
        
    hypotenuse = calculate_hypotenuse(side_1, side_2)
    print(f"The length of the hypotenuse is {hypotenuse} units.")
    print()

    distance = get_positive_number("Please enter the distance traveled (in kilometers): ")

    total = total_fare(distance)
    print(f"The cost of the fare is ${total:.2f}")
    print()

    items_purchased = get_positive_number("Please enter the number of items purchased: ")

    charge = shipping_charge(items_purchased)
    print(f"The shipping charge is ${charge:.2f}")
    print()

    first_value = get_valid_number("Please enter the first number: ")
    second_value = get_valid_number("Please enter the second number: ")
    third_value = get_valid_number("Please enter the third number: ")

    median = calculate_median(first_value, second_value, third_value)
    print(f"The median of these three numbers is {median}")
    print()

    while True:
        try:
            number = int(input("Please enter an integer: "))
            if 1 <= number <= 12:
                break
            else:
                print("The integer must be between 1 and 12.")
                print()
        except ValueError:
            print("INVALID INPUT")
            print()
    ordinal = ordinal_number(number)
    print(f"The ordinal number of {number} is {ordinal}.")
    

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


def get_positive_number(prompt: str) -> float:
    """Gets a positive number (excluding 0) as user input.

    Args:
        prompt: The message the user sees when prompted to type a number.
    
    Returns:
        A positive number (excluding 0).
    """
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                raise ValueError
            break
        except ValueError:
            print("INVALID INPUT")
            print()
    return number


def get_valid_number(prompt: str) -> float:
    """Gets a number as user input.

    Args:
        prompt: The message the user sees when prompted to type a number.

    Returns:
        A number.
    """
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("INVALID INPUT")
            print()
    return value


def test_suite():
    hypotenuse = calculate_hypotenuse(3, 4)
    assert hypotenuse == 5
    hypotenuse = calculate_hypotenuse(4, 3)
    assert hypotenuse == 5
    hypotenuse = calculate_hypotenuse(12, 16)
    assert hypotenuse == 20

    fare_cost = total_fare(0.14)
    assert fare_cost == 4.25
    fare_cost = total_fare(0.3)
    assert fare_cost == 4.5
    fare_cost = total_fare(1)
    assert fare_cost == 5.75

    shipping_cost = shipping_charge(1)
    assert shipping_cost == 10.95
    shipping_cost = shipping_charge(20)
    assert shipping_cost == 67
    shipping_cost = shipping_charge(4)
    assert shipping_cost == 19.8

    median = calculate_median(-1, 0, -2)
    assert median == -1
    median = calculate_median(103, 123, 219)
    assert median == 123
    median = calculate_median(423, -123, 186)
    assert median == 186

    ordinal = ordinal_number(1)
    assert ordinal == "first"
    ordinal = ordinal_number(12)
    assert ordinal == "twelfth"  
    ordinal = ordinal_number(6)
    assert ordinal == "sixth"

if __name__ == "__main__":
    main()
    test_suite()
