# Coding Practice
# November 20, 2020

print("Problem 1")
colour = input("Please enter your favourite colour: ")
print(f"{colour}?! No way, that's my favourite colour too!")

print()
print("Problem 2")
number_of_cans_per_pack = int(input("Please enter the number of cans in the pack: "))
number_of_packs = int(input("Please enter the number of packs: "))
number_of_cans = number_of_cans_per_pack * number_of_packs
print(f"There are {number_of_cans} cans in total.")

print()
print("Problem 3")
first_dimension = float(input("Please enter the first dimension of the rectangular prism: "))
second_dimension = float(input("Please enter the second dimension of the rectangular prism: "))
third_dimension = float(input("Please enter the third dimension of the rectangular prism: "))
total_volume = first_dimension * second_dimension * third_dimension
print(f"The volume of this rectangular prism is {total_volume} units cubed.")

print()
print("Problem 4")
answer = input("Do you just join a Google Meet and mute the teacher? ")
if answer == "yes" or answer == "Yes":
    print("That's probably not a good idea")
elif answer == "no" or answer == "No":
    print("Ok. Good.")
else:
    print("That is not a valid answer!")
