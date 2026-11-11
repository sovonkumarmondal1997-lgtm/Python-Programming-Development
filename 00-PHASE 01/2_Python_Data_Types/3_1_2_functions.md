# Python Functions Notes (Part 1)

# File Name

## `3_1_functions.ipynb`

---

# Important Concepts of Functions

## 1. What is a Function?

A **function** is a reusable block of code that performs a specific task. It executes only when it is called and can receive input values (parameters) and optionally return a result.

---

## 2. Different Types of Functions

### Built-in Functions

Functions already provided by Python.

Examples:

* `print()`
* `len()`
* `sum()`
* `max()`
* `min()`
* `type()`

### User-defined Functions

Functions created by programmers using the `def` keyword.

Example:

```python
def greet():
    print("Hello")
```

---

## 3. Principles of Functions

### 1. DRY (Don't Repeat Yourself)

Avoid writing the same code multiple times.

---

### 2. Modularity

Break a large program into smaller independent functions.

---

### 3. Reusability

Write a function once and use it many times.

---

### 4. Abstraction

Hide implementation details and expose only what the user needs.

---

### 5. Maintainability

Smaller functions are easier to modify, debug, and extend.

---

## 4. Components of a Function

Every function generally contains:

* Function definition (`def`)
* Function name
* Parameters (optional)
* Docstring (optional but recommended)
* Function body
* Return statement (optional)
* Function call
* Arguments

---

# Function Analysis

---

## Function: Let's create a simple function that takes two numbers as input and returns their sum with docstring.

### Natural Language

This function accepts two numbers and returns their addition.

### Concepts Introduced

* Creating a user-defined function
* `def` keyword
* Parameters
* `return`
* Function call
* Docstring

---

## Function: Functions with docstring (`sum_numbers`)

### Natural Language

This function adds two numbers, stores the result in a variable, and returns it.

### Concepts Introduced

* Returning a variable
* Local variables inside functions
* Writing descriptive docstrings

---

## Function: Odd or Even Function with Docstring

### Natural Language

This function checks whether the given integer is odd or even and validates the input type.

### Concepts Introduced

* Conditional statements inside functions
* Type checking using `type()`
* Returning different values based on conditions
* Input validation

---

## Function: Calling `odd_or_even()` for a Single Number

### Natural Language

This demonstrates how to call a function and store its returned value before printing it.

### Concepts Introduced

* Function calling
* Capturing returned values
* Printing returned results

---

## Function: Calling `odd_or_even()` Using a Loop

### Natural Language

This repeatedly calls the same function for numbers 1 through 10.

### Concepts Introduced

* Reusing functions
* Functions inside loops
* Avoiding duplicate code

---

# Parameters

## Definition

Parameters are variables declared in the function definition that receive values when the function is called.

Example

```python
def greet(name):
```

Here, `name` is the parameter.

---

## Function: Parameter Example (`greet`)

### Natural Language

This function receives a person's name and returns a greeting message.

### Concepts Introduced

* Single parameter
* Returning formatted text
* Receiving external input

---

# Arguments

## Definition

Arguments are the actual values passed into a function during a function call.

Example

```python
greet("Alice")
```

Here `"Alice"` is the argument.

---

## Function: Argument Example

### Natural Language

This calls the `greet()` function by passing an actual value.

### Concepts Introduced

* Difference between parameters and arguments
* Passing values to functions

---

# Types of Arguments

Python supports four main argument types.

---

## 1. Positional Arguments

Values are assigned according to the order of parameters.

Example

```python
multiply(5,3)
```

---

## Function: Positional Argument Example (`multiply`)

### Natural Language

This function multiplies two numbers where the first argument goes to the first parameter and the second argument goes to the second parameter.

### Concepts Introduced

* Positional mapping
* Order matters

---

## 2. Keyword Arguments

Arguments are assigned using parameter names.

Example

```python
divide(y=5, x=10)
```

---

## Function: Keyword Argument Example (`divide`)

### Natural Language

This function divides two numbers while allowing arguments to be passed in any order using parameter names.

### Concepts Introduced

* Keyword arguments
* Order does not matter
* Improved readability

---

## 3. Default Arguments

Parameters are assigned default values.

Example

```python
def power(base, exponent=2):
```

---

## Function: Default Argument Example (`power`)

### Natural Language

This function calculates powers and automatically squares the number if no exponent is supplied.

### Concepts Introduced

* Optional parameters
* Default parameter values
* Function flexibility

---

## 4. Variable-Length Arguments

Used when the number of arguments is unknown.

Two types:

* `*args`
* `**kwargs`

---

# *args

## Definition

`*args` collects multiple positional arguments into a tuple.

Example

```python
def func(*args):
```

---

## Function: `sum_all(*args)`

### Natural Language

This function accepts any number of numeric arguments and returns their total.

### Concepts Introduced

* Variable-length positional arguments
* Tuple packing
* Using Python's built-in `sum()`

---

## Function: `multiply_all(*args)`

### Natural Language

This function multiplies all supplied numbers together regardless of how many values are passed.

### Concepts Introduced

* Manual aggregation
* Iterating over `*args`
* Running product pattern

---

# **kwargs

## Definition

`**kwargs` collects keyword arguments into a dictionary.

Example

```python
def func(**kwargs):
```

---

## Function: `print_info(**kwargs)`

### Natural Language

This function prints every keyword argument as a key-value pair.

### Concepts Introduced

* Variable-length keyword arguments
* Dictionary traversal
* `.items()` iteration

---

# Difference Between `return` and `print`

## `return`

* Sends a value back to the caller.
* Can be stored in variables.
* Can be reused in other calculations.
* Ends the function immediately.

Example

```python
return a + b
```

---

## `print`

* Displays output on the screen.
* Does not return useful data.
* Cannot be reused in calculations.

Example

```python
print(a+b)
```

---

## Function: Return vs Print Example

### Natural Language

One function only displays the answer, while the other returns the answer so it can be reused elsewhere.

### Concepts Introduced

* Difference between displaying and returning values
* Importance of `return` in reusable functions

---

# Important Patterns Learned

## Pattern 1 — Basic Function

```python
def function_name(parameters):
    return value
```

---

## Pattern 2 — Function Call

```python
result = function_name(arguments)
```

---

## Pattern 3 — Parameter

```python
def greet(name):
```

---

## Pattern 4 — Argument

```python
greet("Alice")
```

---

## Pattern 5 — Positional Argument

```python
multiply(5,3)
```

---

## Pattern 6 — Keyword Argument

```python
divide(x=10,y=5)
```

---

## Pattern 7 — Default Argument

```python
def power(base, exponent=2):
```

---

## Pattern 8 — *args

```python
def func(*args):
```

---

## Pattern 9 — **kwargs

```python
def func(**kwargs):
```

---

## Pattern 10 — Return

```python
return value
```

---

# Common Interview Questions

### What is a function?

A reusable block of code that performs a specific task.

---

### Difference between parameter and argument?

* Parameter → Variable in function definition.
* Argument → Actual value passed during function call.

---

### Difference between `return` and `print`?

* `return` gives a value back.
* `print` only displays output.

---

### What is a docstring?

A string placed immediately below a function definition that explains what the function does, its parameters, and its return value.

---

### What is `*args`?

Collects multiple positional arguments into a tuple.

---

### What is `**kwargs`?

Collects multiple keyword arguments into a dictionary.

---

### When should default arguments be used?

When a parameter should have a commonly used value if the caller doesn't provide one.

---

# Revision Summary

After completing `3_1_functions.ipynb`, you have learned:

* What functions are
* Why functions are used
* Function principles (DRY, Modularity, Reusability, Abstraction, Maintainability)
* Components of a function
* Function definition
* Function calling
* Parameters
* Arguments
* Docstrings
* Input validation
* Conditional logic inside functions
* Positional arguments
* Keyword arguments
* Default arguments
* Variable-length arguments
* `*args`
* `**kwargs`
* Difference between `return` and `print`
* Writing reusable and maintainable functions
