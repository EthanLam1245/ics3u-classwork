def main():
    string = input("Please enter the string: ")
    while True:
        try:
            width = int(input("Please enter the width of the terminal: "))
            break
        except ValueError:
            print("INVALID INPUT - Enter an integer.")
            print()

    centered_string = center_string(string, width)
    print(centered_string)


def center_string(string: str, width_of_terminal: int) -> str:
    """Centers a string based on a width.

    Args:
        string: A string entered gotten as user input.
        width_of_terminal: An integer that determines where the string will be centered.
    
    Returns:
        A new string consisting of the original string and the correct number of leading spaces.
    """
    new_string = ""
    width_of_terminal -= len(string)
    i = 0
    while i < width_of_terminal // 2:
        new_string += " "
        i += 1
    new_string += string
    return new_string


def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    print("all passed!")


if __name__ == "__main__":
    main()
    tests()
