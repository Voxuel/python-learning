# Functions

In programming we often want to re-use code to not have to type the same stuff over and over again.
Functions is taken from math where they are also called functions, In the same way we say:

"The function of x" as example where we have: f(x)

In programming we **define** a function in the way so it has this body:

```text
Visability (Only in some languages like C#/C++/Java) | Return type | Function name | Paramters
```

Let's break down each of the parts of a function decloration: 

### Visability

Vissability means how the rest of the program can see and call the function, In most languages we have these types:

- Public - The whole program can access this function
- Private - Only the file/class/struct can access this function
- Internal (Few languages) - Only the class and it's inherited memebers can access it.

### Return Type

Return type means what data type the function will give back when it returns its result. Different languages show the return type in different ways, Let's look at some examples

In C++

```c++
int sum(int x, int y) {
    return x + y;
}
```

Here we can see that the return type is of type **int** meaning the function will return a integer value.

In python we show the return type a bit differently like so:

```python
def sum(x: int, y: int) -> int:
    return x + y
```

We use the "def function_name(parameters...) -> (return type)" in python

Same function but the function definition is a bit different as we have the return type last. But both functions still return a integer.

We set the return type for multiple reasons:

- To make it easier for someone else using our function to know what the outcome of it will be.
- Some languages require us to set it otherwise it will not be valid syntax (Python does NOT require it but it's best practice to set it anyways to make your code more readable)
- For type validation, So when you try to pass the value from a function to another function, It will detect beforehand if the value you are sending is the expected one and not something else.

A function can also return nothing:

```python
def send_hello_message() -> None:
    print("Hello!")
```

### Function name

The function name is the **identifier** of the function. This is what we use to call the function elsewhere in our code.

It might seem like the function name is just something we use to call it with but the name have some important parts:

- A function name should be **self-explinatory**, Meaning that the name should describe what the function does, take these examples:


```python
def f(author1: str, author2: str) -> list[str]:
    return [author1, author2]
```
This is a very bad name, as we have no clue outside what the function does, we only know it returns a list of strings, but why? or of what?

Instead we should do:
```python
def generate_authors_list(author1: str, author2: str) -> list[str]:
    return [author1, author2]
```
In this example we know when the user calls the function that it will create a new list of the users favorit authors in the form of a list of string variables of the names of each author.

Naming functions has always been one of the hardest parts for programmers and it's a art in a way to create good function names, This is something we learn over time as our experience grows. The general rules are:

- The name should explain what it does.
- The name should not explain in the smallest detail at the same tile, as example:

Good name: **generate_authors_list**

Bad name: **create_new_list_of_favorit_authors_for_the_user***


### Parameters

The parameters are the values or data we send to a function that the function needs to perform it's action. Let's take the "[sum](#return-type)" example from before, That function takes 2 parameters, **x** and **y** and then adds them togheter.


When using functions we as we said before avoid doing repeated operations and can instead call the same function multiple times with different parameters, So it would look like:

```python
result1 = sum(1,1) # returns 2
result2 = sum(100,100) # returns 200
```

We also want to define which the data type is for the parameters, This is as well NOT mandatory in python but is best practice to do so, This makes it easier for both the function to handle the parameters it is given but also for the user of the function to know what the function expects.

A function can also take no parameters:

```python
def get_current_temperature() -> float:
    temp = 13.5f
    return temp
```


### Lastly

There are some rules when it comes to functions in python:

- A function name should never be reapeted in the same file.
- A function name should never have the same name as a funcction in the python builtin library (More on this later)
- A function should only do **one** thing, Creating large and complex functions makes readability much harder and debugging sometimes very complex, Simplicity over complexity. If your function is starting to get to complex and long, then break it down into smaller functions instead.

# Side task

Create 3 functions, one for addition, one for subtraction and one for multiplication. Make sure the return types and parametrs in are correct. Then follow these rules:

- Each function should only do 1 thing, You should even be able to make each function body just 1 line.
- What happens if a user sends numbers with decimals? like 0,3? Think about the parameters and return types data types. could we use another type?
- Think about how input in python works, if you run the application and input for addition 3 and 5, Does that work? or do you maybe need to change the data type of the input from the user to a fitting type before passing it to the function?
