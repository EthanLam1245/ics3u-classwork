# Coding Practice
# November 20, 2020

print("Problem 1")
Colour = input("Please enter your favourite colour: ")
print(f"{Colour}?! No way, that's my favourite colour too!")

print()
print("Problem 2")
NumberOfCansPerPack = int(input("Please enter the number of cans in the pack: "))
NumberOfPacks = int(input("Please enter the number of packs: "))
NumberOfCans = NumberOfCansPerPack*NumberOfPacks
print(f"There are {NumberOfCans} cans in total.")

print()
print("Problem 3")
FirstDimension = float(input("Please enter the first dimension of the rectangular prism: "))
SecondDimension = float(input("Please enter the second dimension of the rectangular prism: "))
ThirdDimension = float(input("Please enter the third dimension of the rectangular prism: "))
TotalVolume = FirstDimension*SecondDimension*ThirdDimension
print(f"The volume of this rectangular prism is {TotalVolume} units cubed.")

print()
print("Problem 4")
Answer = input("Do you just join a Google Meet and mute the teacher? ")
if Answer == "yes" or Answer == "Yes":
    print("That's probably not a good idea")
elif Answer == "no" or Answer == "No":
    print("Ok. Good.")
else:
    print("That is not a valid answer!")

