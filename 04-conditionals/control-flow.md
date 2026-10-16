# Conditionals and Control flow

In programming we usually want to control in which direction the program takes or which choices it makes depending on certain criterias or events. We call this conditionals or control flow.

In python we have some different ways to do conditionals. The main way is "if-statments".

## Indentation: grouping instructions

Python uses spaces at the start of a line, called **indentation**, to show which instructions belong together. After an `if` condition, write a colon (`:`), then indent the instructions that should run when the condition is true. By convention, use four spaces for each level of indentation.

```python
is_sunny = True

if is_sunny:
    print("Wear sunglasses")

print("This line runs after the if block")
```

The indented `print()` belongs to the `if` block, so it runs only when `is_sunny` is true. The last `print()` is not indented, so it is outside the block and runs either way. Keep the indentation consistent; Python uses it to understand the program.

Say we take input from the user about how old they are and we only want people over the age of 15 use our application. We could check this like this:

```python
users_age = int(input("How old are you? "))

# we check the input from the user first with a "if"

# if the users age is MORE or EQUAL to 15, we let them into the application
# However, if the user is below the age of 15, we want to stop the application, we do this with a "else"

if users_age >= 15:
    print("Welcome to the application!")
else:
    print("You need to be 15 or older!")
    exit()

```

Conditionals work in the way of "Is something true? if so do this, otherwise do that"

But what if we have multiple different possible outcomes? Say we want to tell the user a different message depending on what their favorit food is. We can do this with "elif"

```python
favorit_food = input("What is your favorit food?")

if favorit_food == "Hamburger":
    print("I also like hamburgers!")
elif favorit_food == "Pizza":
    print("Pizza is really good!")
elif favorit_food == "Sushi":
    print("I have only had Sushi once")
else:
    print(f"{favorit_food} is great favorit food!")

```

In the above example we check for the foods: "Hamburger", "Pizza" and "Sushi".
If the user gave any of the 3 we give them a custom message about that specific food otherwise we just say a generic message to them back.

## Combining conditions with `and` and `or`

Sometimes a decision depends on more than one thing. Python's `and` and `or` let us combine conditions:

- `and` means **both conditions must be true**.
- `or` means **at least one condition must be true**. Both can be true, too.

### Using `and`

This example welcomes someone only if they are at least 18 **and** they have a car. Both checks must pass:

```python
users_age = int(input("How old are you? "))
has_car = input("Do you have a car? ") == "yes"

if users_age >= 18 and has_car:
    print("Let's get started!")
else:
    print("Both requirements must be met.")
```

If either check is false, the whole `and` condition is false.

### Using `or`

This example gives a special message if the favorite food is **either** pizza **or** a hamburger:

```python
favorite_food = input("What is your favorite food? ")

if favorite_food == "Pizza" or favorite_food == "Hamburger":
    print("That's one of my favorites, too!")
else:
    print("That sounds good!")
```

If either check is true, the whole `or` condition is true. The answers in this example must match the capitalization shown.

### ***Side task***
Create a program inside **conditionals.py** that lets the user sign up for a driving license. Ask the user:

- What is their name
- What is their age
- Do they have a Car

We have some rules:

- if the user is underneath 18 years old we need to say: "Sorry, come back when you are older!"
- if the user is 18 or older and do NOT have a Car we say: "Sorry come back when you have a car!"
- if the user is 18 or older and has a car, say: "Let's get licensed!"
