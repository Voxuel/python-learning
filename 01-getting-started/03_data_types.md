# Data types

When we create programs, we work with different kinds of information. In Python, each value has a **data type**. The type tells Python what kind of value it is and what we can do with it.

For example, we can do arithmetic with numbers, join pieces of text, or group several values together.

| Type | What it is | Example | Helpful to know |
| --- | --- | --- | --- |
| `str` (string) | Text, such as a name or a message. | `"Hello!"` or `'Hello!'` | Put text inside matching single or double quotes. |
| `int` (integer) | A whole number, with no decimal part. | `7`, `0`, `-3` | Use integers for things like a number of students or apples. |
| `float` | A number that can have a decimal part. | `3.14`, `-0.5` | Use a dot for the decimal point. |
| `bool` (Boolean) | A value that is either true or false. | `True` or `False` | These values are often used to make decisions. Their first letters must be capitalized. |
| `list` | An ordered group of values. | `["apple", "pear", "plum"]` | Use square brackets. A list can hold multiple values. |
| `tuple` | An ordered group of values that is not meant to be changed. | `(10, 20)` | Use parentheses. You can learn this after lists. |
| `dict` (dictionary) | A group of named values, stored as key-value pairs. | `{"name": "Sam", "age": 12}` | Use braces. Here, `"name"` and `"age"` are keys that label their values. |
| `set` | A group of values where each value appears only once. | `{"red", "blue"}` | Use braces. Sets are useful when you only care which values are present, not their order. |
| `NoneType` | The type of the special value `None`, which means no value is available. | `None` | `None` is different from `0`, `False`, and empty text (`""`). |

The examples above are values. You can store a value in a variable, for example:

```python
student_name = "Sam"
student_age = 12
is_enrolled = True
```

Python can often work out a value's type for you. You can ask Python to show it with `type()`:

```python
print(type(student_name))  # <class 'str'>
print(type(student_age))   # <class 'int'>
```

Data types also have a important role when it comes to combining data. As example.

We can do:

```python
# integer variable
variable1 = 1
variable2 = 1

variable3 = variable1 + variable2

print(variable3) # Will print "2"
```

but we cannot do:

```python
# integer variable
variable1 = 1
# string variable
variable2 = "This is text"

variable3 = variable1 + variable2
# Will crash with Exception:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Since it does not make sense to try and do addition of a peice of text and a number.
