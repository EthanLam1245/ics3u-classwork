import math

# CONSTANTS
base_fare = 4
variable = 0.25

first_item = 10.95
subsequent_items = 2.95

# MAIN FUNCTION
def main():
    valid = False
    while valid == False:
        try:
            side_1 = float(input("Please enter the first shortest side: "))
            side_2 = float(input("Please enter the second shortest side: "))
            hypotenuse = calculate_hypotenuse(side_1, side_2)
            print(f"The length of the hypotenuse is {hypotenuse}")
            valid = True
        except ValueError:
            print("INVALID INPUT")
        print()

    valid = False
    while valid == False:
        try:
            distance = float(input("Please enter the distance traveled (in kilometers): "))
            total = total_fare(distance)
            print(f"The cost of the fare is ${total:.2f}")
            valid = True
        except ValueError:
            print("INVALID INPUT")
        print()

    valid = False
    while valid == False:
        try:
            items_purchased = int(input("Please enter the number of items purchased: "))
            charge = shipping_charge(items_purchased)
            print(f"The shipping charge is ${charge:.2f}")
            valid = True
        except ValueError:
            print("INVALID INPUT")
        print()

    valid = False
    while valid == False:
        try:
            first_value = float(input("Please enter the first number: "))
            second_value = float(input("Please enter the second number: "))
            third_value = float(input("Please enter the third number: "))
            median = calculate_median(first_value, second_value, third_value)
            print(f"The median of these three numbers is {median}")
            valid = True
        except ValueError:
            print("INVALID INPUT")
        print()

    valid = False
    while valid == False:
        try:
            number = int(input("Please enter an integer: "))
            ordinal = ordinal_number(number)
            if ordinal != "":
                print(f"The ordinal number of {number} is {ordinal}.")
                valid = True
            else:
                print("The integer must be between 1 and 12.")
                print()
        except ValueError:
            print("INVALID INPUT")
            print()
    

#Exercise 81: Compute the Hypotenuse
def calculate_hypotenuse(first_side: float, second_side: float) -> float:
    return math.sqrt(first_side ** 2 + second_side ** 2)


#Exercise 82: Taxi Fare
def total_fare(distance_traveled: float) -> float:
    multiplier = int(str(distance_traveled * 1000 / 140)[0])
    return base_fare + variable * multiplier


#Exercise 83: Shipping Calculator
def shipping_charge(number_of_items: int) -> float:
    if number_of_items > 0:
        return first_item + subsequent_items * (number_of_items - 1)
    else:
        return 0


#Exercise 84: Median of Three Values
def calculate_median(num1: float, num2: float, num3: float) -> float:
    unsorted = [num1, num2, num3]
    largest = max(unsorted)
    smallest = min(unsorted)
    unsorted.remove(largest)
    unsorted.remove(smallest)
    return unsorted[0]


#Exercise 85: Convert an Integer to its Ordinal Number
def ordinal_number(integer: int) -> str:
    english_ordinal_numbers = "first second third fourth fifth sixth seventh eight ninth tenth eleventh twelfth".split(" ")
    if 1 <= integer <= 12:
        return english_ordinal_numbers[integer - 1]
    else:
        return ""


if __name__ == "__main__":
   main()
