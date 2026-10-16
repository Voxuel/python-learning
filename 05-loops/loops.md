# Loops

Programs often need to repeat an action. You could write the same instruction many times, but that gets messy. A **loop** lets Python repeat a set of instructions for you.

Python has two main kinds of loops: `while` loops and `for` loops.

## `while` loops

A `while` loop repeats as long as a condition is true. For example, this loop counts down from 3:

```python
number_of_times = 3

while number_of_times > 0:
    print(f"The number is now: {number_of_times}")
    number_of_times = number_of_times - 1

print("The loop has finished.")
```

The output is:

```text
The number is now: 3
The number is now: 2
The number is now: 1
The loop has finished.
```

Python checks `number_of_times > 0` before each repetition. Each time through the loop, the number gets smaller. When it reaches `0`, the condition is false and the loop ends.

The indented lines belong to the loop. They run again each time the loop repeats. The final `print()` is not indented, so it runs once after the loop ends.

### Avoiding an endless loop

Make sure a `while` loop can eventually become false. If the value in its condition never changes, the loop may run forever:

```python
number = 3

while number > 0:
    print(number)
```

This example never changes `number`, so `number > 0` stays true. Add an update inside the loop, such as `number = number - 1`, to make it stop.

## `for` loops

A `for` loop is useful when you want to repeat something for each item in a group, or a known number of times. `range()` can provide a sequence of numbers:

```python
for number in range(1, 4):
    print(number)
```

The output is:

```text
1
2
3
```

`range(1, 4)` starts at `1` and stops before `4`. The indented instruction runs once for each number.

If you only give `range()` one number, it starts counting at `0` and stops before that number:

```python
for count in range(3):
    print("Hello!")
```

This prints `Hello!` three times. The values from `range(3)` are `0`, `1`, and `2`.

## Which loop should I use?

- Use a `for` loop when you know how many times to repeat, or when you want to go through a group of items.
- Use a `while` loop when you want to repeat until a condition changes, such as waiting for the user to enter the right answer.


## Exercise: Repeat a greeting

Create a program that asks the user for their name and how many times they want to see a greeting. Use a `for` loop to print the greeting that many times.

For example, if the user enters `Mina` and `3`, the program should display:

```text
Hello, Mina!
Hello, Mina!
Hello, Mina!
```

Hints:

- `input()` gives you text. Convert the number of repetitions to an integer with `int()`.
- Use `range()` to repeat the greeting the requested number of times.
- Bonus: use a `while` loop to count down from the number the user entered, then print `Done!`.



