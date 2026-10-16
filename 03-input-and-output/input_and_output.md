# Input and output

Programs can show information to a person and ask that person for information. These are called **output** and **input**.

- **Output** is information the program shows, such as a message on the screen.
- **Input** is information a person gives to the program, such as their name.

## Showing output with `print()`

Use `print()` to show text or a value on the screen:

```python
print("Hello!")
print(42)
```

The output is:

```text
Hello!
42
```

Python moves to a new line after each `print()` call.

## Asking for input with `input()`

Use `input()` to ask a question. The person's answer is returned by `input()` so you can store it in a variable:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

When you run this program, it pauses at the question until you type an answer and press Enter. The answer is stored in `name` and then used in the greeting.

The `f` before the quotation mark lets you put a variable inside text using curly braces, like `{name}`. This is called an **f-string**.

## Input is text

Even if someone types a number, `input()` gives the program text (a string). To do arithmetic with that answer, convert it to a number with `int()`:

```python
age_text = input("How old are you? ")
age = int(age_text)
print(f"Next year, you will be {age + 1}.")
```

For this example, enter a whole number such as `12`. `int()` converts text containing a whole number into an integer. If the answer is not a whole number, Python will show an error; we will learn how to handle errors later.

## Try it

Run `input_and_output.py` in this folder. Enter your name, a food you like, and your age. The program will greet you and tell you how old you will be next year.

You can run it from the repository's main folder with:

```sh
uv run 03-input-and-output/input_and_output.py
```

On Windows, use:

```powershell
uv run 03-input-and-output/input_and_output.py
```
