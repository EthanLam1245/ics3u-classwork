import math


# CONSTANTS
base_fare = 4
variable = 0.25

first_item = 10.95
subsequent_items = 2.95

# MAIN FUNCTION
def main():
    while True:
        try:
            side_1 = float(input("Please enter the first shortest side: "))
            if side_1 <= 0:
                raise ValueError
            side_2 = float(input("Please enter the second shortest side: "))
            if side_2 <= 0:
                raise ValueError
            break
        except ValueError:
            print("INVALID INPUT")
            print()

    hypotenuse = calculate_hypotenuse(side_1, side_2)
    print(f"The length of the hypotenuse is {hypotenuse} units.")
    print()

    while True:
        try:
            distance = float(input("Please enter the distance traveled (in kilometers): "))
            if distance < 0:
                raise ValueError
            total = total_fare(distance)
            break
        except ValueError:
            print("INVALID INPUT")
            print()
    
    print(f"The cost of the fare is ${total:.2f}")
    print()

    while True:
        try:
            items_purchased = int(input("Please enter the number of items purchased: "))
            if items_purchased < 0:
                raise ValueError
            break
        except ValueError:
            print("INVALID INPUT")
            print()

    charge = shipping_charge(items_purchased)
    print(f"The shipping charge is ${charge:.2f}")
    print()

    while True:
        try:
            first_value = float(input("Please enter the first number: "))
            second_value = float(input("Please enter the second number: "))
            third_value = float(input("Please enter the third number: "))
            break
        except ValueError:
            print("INVALID INPUT")
            print()

    median = calculate_median(first_value, second_value, third_value)
    print(f"The median of these three numbers is {median}")
    print()

    while True:
        try:
            number = int(input("Please enter an integer: "))
            ordinal = ordinal_number(number)
            if ordinal != "":
                print(f"The ordinal number of {number} is {ordinal}.")
                break
            else:
                print("The integer must be between 1 and 12.")
                print()
        except ValueError:
            print("INVALID INPUT")
            print()
    

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
    multiplier = int(str(distance_traveled * 1000 / 140)[0])
    return base_fare + variable * multiplier


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
        integer: An integer between 1 and 12 (inclusive)
    
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
