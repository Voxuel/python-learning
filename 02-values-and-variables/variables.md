# Variables

Variables give values names so we can use them later. They help us reuse information, make code easier to read, and change a value in one place.

Imagine you have a book you want to show on several websites. Instead of writing the whole book each time, you can store its text in a variable and use that name wherever you need it:

```python
book_text = "The book text goes here."

print(book_text)
print(book_text)
print(book_text)
```

Each `print(book_text)` uses the value stored in `book_text`. In a real program, `print()` displays text on the screen; it does not send anything to a website.

## Creating a variable

Use an equals sign (`=`) to give a variable a value. This is called **assignment**:

```python
student_name = "Mina"
student_age = 12
```

Read each line from right to left: Python works out the value on the right, then stores it under the name on the left. The equals sign here means “store this value in this variable.”

You can use a variable by writing its name:

```python
print(student_name)
print(student_age)
```

The output is:

```text
Mina
12
```

## Changing a value

A variable can be given a new value. The new value replaces the old one:

```python
score = 10
print(score)

score = 15
print(score)
```

The output is `10` and then `15`. The variable `score` has one current value at a time.

You can also use the current value to calculate a new one:

```python
score = score + 5
print(score)
```

This adds 5 to the current value of `score`, then stores the result back in `score`.

## Choosing variable names

A good name helps people understand what a value is for. Python programmers commonly use lowercase words separated by underscores (snake_case):

```python
book_title = "A Short Story"
page_count = 24
```

Remember these basic rules:

- A name can contain letters, numbers, and underscores (`_`).
- A name cannot start with a number. Use `page2`, not `2page`.
- Names are case-sensitive: `student_name` and `Student_Name` are different names.
- Choose a name that describes the value, such as `temperature` instead of `x`.
- Do not use Python's reserved words, such as `if`, `for`, or `class`, as variable names.

## Variables can hold different types

A variable can store text, a whole number, a decimal number, or another kind of value. Python figures out the type from the value you assign:

```python
name = "Mina"
age = 12
height = 1.5
is_student = True
```

Here, `name` holds text (`str`), `age` a whole number (`int`), `height` a decimal number (`float`), and `is_student` a true-or-false value (`bool`). Text needs quotes; numbers and `True`/`False` do not.