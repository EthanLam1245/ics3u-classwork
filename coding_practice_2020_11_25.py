# The Python Workbook (10 questions)
#Exercise 34
integer = int(input("Please enter an integer: "))
if integer % 2 == 0:
    print("This is an even number.")
elif integer % 2 == 1:
    print("This is an odd number.")

#Exercise 35
print()
human_years = float(input("Please enter the number of human years for conversion: "))
if 0 <= human_years <= 2:
    dog_years = human_years * 10.5
    print(f"This is the same as {dog_years} dog years.")
elif human_years > 2:
    dog_years = 21 + (human_years - 2) * 4
    print(f"This is the same as {dog_years} dog years.")
else:
    print("The number you have entered is invalid.")

#Exercise 36
print()
letter = input("Please enter a letter of the alphabet: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The entered letter is a vowel.")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print("The entered letter is a consonant.")

#Exercise 37
print()
number_of_sides = int(input("Please enter the number of sides this shape has: "))
if 2 < number_of_sides < 11:
    if number_of_sides == 3:
        shape = "Triangles"
    elif number_of_sides == 4:
        shape = "Quadrilaterals"
    elif number_of_sides == 5:
        shape = "Pentagons"
    elif number_of_sides == 6:
        shape = "Hexagons"
    elif number_of_sides == 7:
        shape = "Heptagons"
    elif number_of_sides == 8:
        shape = "Octagons"
    elif number_of_sides == 9:
        shape = "Nonagons"
    elif number_of_sides == 10:
        shape = "Decagons"
    print(f"{shape} have {number_of_sides} sides.")
else:
    print(f"A {number_of_sides} sided shape cannot be named.")

#Exercise 38
print()
name_of_month = input("Please enter the name of a month: ")
name_of_month_lower = name_of_month.lower()
if name_of_month_lower == "january" or name_of_month == "march" or name_of_month == "may" or name_of_month == "july" or name_of_month == "august" or name_of_month == "october" or name_of_month == "december":
    print(f"{name_of_month} has 31 days.")
elif name_of_month_lower == "april" or name_of_month == "june" or name_of_month == "september" or name_of_month == "november":
    print(f"{name_of_month} has 30 days.")
elif name_of_month_lower == "february":
    print(f"{name_of_month} has 28 or 29 days.")
else:
    print(f"{name_of_month} is not a month.")

#Exercise 39
print()
sound_level = float(input("Please enter the number of decibels: "))
sound = ""
if sound_level < 40:
    print(f"A decibel level of {sound_level} is quieter than a quiet room.")
elif sound_level > 130:
    print(f"A decibel level of {sound_level} is louder than a jackhammer.")
else:
    if sound_level == 130:
        sound = "of a jackhammer"
    elif sound_level == 106:
        sound = "of a gas lawnmower"
    elif sound_level == 70:
        sound = "of an alarm clock"
    elif sound_level == 40:
        sound = "of a quiet room"
    elif 40 < sound_level < 70:
        sound = "between a quiet room and an alarm clock"
    elif 70 < sound_level < 106:
        sound = "betweem an alarm clock and a gas lawnmower"
    elif 106 < sound_level < 130:
        sound = "between a gas lawnmower and a jackhammer"
    print(f"A decibel level of {sound_level} is the sound level {sound}.")

#Exercise 40
print()
side_1 = float(input("Please enter the first side length of the triangle: "))
side_2 = float(input("Please enter the second side length of the triangle: "))
side_3 = float(input("Please enter the third side length of the triangle: "))
triangle_type = ""
if side_1 == side_2 == side_3:
    triangle_type = "an equilateral triangle"
elif side_1 == side_2 != side_3 or side_1 == side_3 != side_2 or side_1 != side_2 == side_3:
    triangle_type = "an isosceles triangle"
else:
    triangle_type = "a scalene triangle"
print(f"A triangle with the side lengths {side_1}, {side_2}, and {side_3} is {triangle_type}.")

#Exercise 41
print()
note_name = input("Please enter the name of a note: ")
frequency = float
octave = int(note_name[1])
if note_name[0] == "C":
    frequency = 261.63
elif note_name[0] == "D":
    frequency = 293.66
elif note_name[0] == "E":
    frequency = 329.63
elif note_name[0] == "F":
    frequency = 349.23
elif note_name[0] == "G":
    frequency = 392.00
elif note_name[0] == "A":
    frequency = 440.00
elif note_name[0] == "B":
    frequency = 493.88
frequency = frequency / 2 ** (4 - octave)
print(f"The frequency of this note is {frequency}Hz")

#Exercise 42
print()
input_frequency = float(input("Please enter a frequency in Hertz: "))
note = ""
if 260.63 <= input_frequency <= 262.63:
    note = "C"
elif 292.66 <= input_frequency <= 294.66:
    note = "D"
elif 328.63 <= input_frequency <= 330.63:
    note = "E"
elif 348.23 <= input_frequency <= 350.23:
    note = "F"
elif 391.00 <= input_frequency <= 393.00:
    note = "G"
elif 439.00 <= input_frequency <= 441.00:
    note = "A"
elif 492.88 <= input_frequency <= 494.88:
    note = "B"

if note == "":
    print(f"A frequency of {input_frequency} Hertz does not correspond to a known note.")
else:
    print(f"Note {note}4 has a frequency of {input_frequency} Hertz.")

#Exercise 43
print()
denomination_of_banknote = float(input("Please enter the denomination of a banknote: $"))
name_of_individual = ""
if denomination_of_banknote == 1:
    name_of_individual = "George Washington"
elif denomination_of_banknote == 2:
    name_of_individual = "Thomas Jefferson"
elif denomination_of_banknote == 5:
    name_of_individual = "Abraham Lincoln"
elif denomination_of_banknote == 10:
    name_of_individual = "Alexander Hamilton"
elif denomination_of_banknote == 20:
    name_of_individual = "Andrew Jackson"
elif denomination_of_banknote == 50:
    name_of_individual = "Ulysses S. Grant"
elif denomination_of_banknote == 100:
    name_of_individual = "Benjamin Franklin"

if name_of_individual == "":
    print(f"A banknote worth ${denomination_of_banknote:.2f} does not exist.")
else:
    print(f"Name of individual that appears on a ${denomination_of_banknote:.2f} banknote: {name_of_individual}")

#CodingBat (10 questions) - done in CodingBat directly
#String-1 Exercise 1 - hello_name

def hello_name(name):
    greeting = "Hello " + name + "!"
    return greeting

#String-1 Exercise 2 - make_abba

def make_abba(a, b):
    combined_string = a + b + b + a
    return combined_string

#String-1 Exercise 3 - make_tags

def make_tags(tag, word):
    HTML = "<{}>{}</{}>".format(tag, word, tag)
    return HTML

#String-1 Exercise 4 - make_out_word

def make_out_word(out, word):
    new_string = out[0:2] + word + out[2:4]
    return new_string

#String-1 Exercise 5 - extra_end

def extra_end(str):
    duplicated_string = 3 * (str[-2] + str [-1])
    return duplicated_string

#String-1 Exercise 6 - first_two

def first_two(str):
    if len(str) >= 2:
        return str[0:2]
    else:
        return str

#String-1 Exercise 7 - first_half

def first_half(str):
    half_of_string = len(str)/2
    return str[0:half_of_string]

#String-1 Exercise 8 - without_end

def without_end(str):
    remove_letters_string = str[1:-1]
    return remove_letters_string

#String-1 Exercise 9 - combo_string

def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

#String-1 Exercise 10 - non_start

def non_start(a, b):
    concatenated_string = a[1:len(a)] + b[1:len(b)]
    return concatenated_string
