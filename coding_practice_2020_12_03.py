# Function Practice
# Question 1
def add_3_numbers(a: float, b: float, c: float) -> float:
    """Adds three numbers together.
    
    Args:
        a: A number
        b: Another number
        c: The third number
       
    Returns:
        The sum of the numbers.
    """
    return a + b + c

sum_of_numbers = add_3_numbers(5.6, 8.2, 12.13)
print(f"The sum of the numbers are {sum_of_numbers}.")
print()

# Question 2
def string_message(name: str, age: int) -> str:
    """Takes a name and an age and returns a stirng message.
    
    Args:
        name: User's name
        age: User's age
       
    Returns:
        A string message with both name and age.
    """
    message = f"Hey {name}! I know you are {age} years old! How are you?"
    return message

string = string_message("Ethan", 15)
print(string)
print()

# Question 3
def average_of_numbers(num1: float, num2: float) -> float:
    """Finds the average of two numbers.
    
    Args:
        num1: A number
        num2: Another number
       
    Returns:
        The average of the numbers.
    """
    average = (num1 + num2) / 2
    return average

resulting_average = average_of_numbers(10.4, 18.3)
print(f"The average of these numbers is about {resulting_average:.2f}.")
print()

# Question 4
def maximum_number(n1: float, n2: float, n3: float) -> float:
    """Finds the maximum value from three numbers.
    
    Args:
        n1: First number
        n2: Second number
        n3: Third number
       
    Returns:
        The largest number of the three.
    """
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        return "undetermined"

largest = maximum_number(1296, 3450.23, 933)
print(f"The largest value of these three numbers is {largest}.")
print()

# Question 5
def first_two(string: str) -> str:
    """Slices the first two characters in a given string.
    
    Args:
        string: A string
       
    Returns:
        The first two characters of the string.
    """
    return string[0:2]

new_string = first_two("Hello World")
print(new_string)
