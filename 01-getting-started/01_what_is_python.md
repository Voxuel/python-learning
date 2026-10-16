# What is Python?

Python is an interpreted programming language.
This means that when we want to run the code, we ask Python to run the file.

Python reads and runs the instructions from top to bottom, like this:

```python
print("I will run first")

print("I will run second")

this_variable_will_then_be_created = "as the 3 step of the program"

print("I am last!")
```

## Interpreted languages

An interpreted language is usually run by another program called an interpreter. For example, you can run a Python file using the Python interpreter.

as example:

python my_program.py (source code that runs directly in your console)

### Benefits

- You can run code quickly without a separate compile step.
- It is often easier to try ideas and see the results right away.
- The same source code can usually run on different operating systems, as long as a compatible interpreter is installed.

### Drawbacks

- Programs may run more slowly than equivalent compiled programs, though the difference depends on the program and language implementation.
- The computer needs the right interpreter installed to run the program.
- Some errors are only discovered when the program reaches the problem while running.

## What is a compiled language?

A compiled language is translated by a compiler into a form the computer can run before the program starts. For example, a compiler can turn C or C++ source code into an executable program. 

as example your programming code (source code):

my_program.c (source code)

becomes:

my_program.exe (binary compiled executable)

### Compared with interpreted languages

- Compiled programs can often run faster, and some errors can be found during compilation.
- Compiling adds an extra step, and the resulting program may need to be built separately for different operating systems or computer types.

