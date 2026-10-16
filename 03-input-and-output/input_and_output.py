print("Let's get to know each other!")

name = input("What is your name? ")
favorite_food = input("What is a food you like? ")
age_text = input("How old are you? ")

# input() gives us text, so convert the age to a whole number before calculating.
age = int(age_text)

print()
print(f"Hello, {name}!")
print(f"You like {favorite_food}.")
print(f"Next year, you will be {age + 1}.")
