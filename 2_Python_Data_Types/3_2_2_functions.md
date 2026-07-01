# Python Functions Notes (Part 2)

# File Name

## `3_2_functions.ipynb`

---

# Important Concepts Covered

This notebook focuses on how functions work internally in Python, variable scope, and why functions are called **First-Class Objects**.

Topics covered:

* Function execution in memory
* Function stack frames
* Default return value (`None`)
* Variable scope
* Local scope
* Global scope
* Enclosing scope
* Main program scope
* Variable shadowing
* Nested functions
* Functions as First-Class Objects
* Function references
* `type()` and `id()` with functions
* Deleting function names
* Functions inside lists and sets
* Returning functions from functions
* Passing functions as arguments (Higher-Order Functions)

---

# Function Execution in Memory

## Concept

Whenever a function is called:

1. Python creates a **new stack frame**.
2. Parameters and local variables are stored inside that frame.
3. The function executes.
4. The frame is destroyed after execution.
5. Local variables disappear from memory.

### Important Concept Introduced

Every function call gets its own independent memory space.

---

# Function: `greet(name)` (Without Return Statement)

### Natural Language

This function prints a greeting message but does not return any value.

### Concepts Introduced

* Function without `return`
* Default return value
* Printing vs returning

### Important Note

If a function does not contain a `return` statement, Python automatically returns

```python
None
```

---

# Variable Scope

## Types of Scope

Python has four important scopes.

### 1. Local Scope

Variables created inside a function.

Accessible only inside that function.

---

### 2. Global Scope

Variables created outside every function.

Accessible throughout the program.

---

### 3. Enclosing Scope

Variables created inside an outer function.

Accessible by nested functions.

---

### 4. Main Program Scope

The top-level scope where the program starts execution.

---

# Function: Local Scope Example (`outer_function()`)

### Natural Language

This function creates an outer variable and an inner function that accesses both the outer and inner variables.

### Concepts Introduced

* Local variables
* Nested functions
* Variable visibility
* Parent-child scope relationship

### Important Observation

Inner functions can access variables from outer functions.

Outer functions **cannot** access variables created inside inner functions.

---

# Function: Global Scope Example (`access_global_variable()`)

### Natural Language

This function prints a variable that was created outside the function.

### Concepts Introduced

* Global variables
* Reading global variables inside functions

### Important Observation

Functions can directly read global variables unless a local variable with the same name exists.

---

# Function: Enclosing Scope Example (`outer_function()`)

### Natural Language

This function demonstrates that an inner function can access variables belonging to its parent function.

### Concepts Introduced

* Enclosing scope
* Nested functions
* Lexical scope

### Important Observation

The enclosing scope sits between the local and global scopes.

---

# Function: Main Program Scope Example (`my_function()`)

### Natural Language

This function accesses a variable defined in the main program.

### Concepts Introduced

* Main program scope
* Accessing top-level variables

---

# Function: Same Variable Name in Local and Global Scope

### Natural Language

This function creates a local variable with the same name as a global variable and prints both separately.

### Concepts Introduced

* Variable shadowing
* Local variables override global variables inside the function

### Important Observation

Python always checks for variables in this order:

1. Local
2. Enclosing
3. Global
4. Built-in

This is called the **LEGB Rule**.

---

# Function: Nested Function Example

### Natural Language

This function defines another function inside itself and calls it.

### Concepts Introduced

* Nested functions
* Function organization
* Scope boundaries

### Important Observation

Inner functions only exist while the outer function is executing.

---

# Functions are First-Class Objects

## Definition

Python treats functions like any other object.

A function can be:

* Stored in variables
* Stored in lists
* Stored in sets
* Passed as arguments
* Returned from another function

---

# Function: `greet(name)` as a First-Class Object

### Natural Language

This function returns a greeting and is assigned to another variable.

### Concepts Introduced

* Function assignment
* Function reference
* First-class objects

### Important Observation

```python
greeting_function = greet
```

No function call happens here.

Only the reference is copied.

---

# Function Analysis: `type(greet)` and `id(greet)`

### Natural Language

This example checks the data type and memory address of a function.

### Concepts Introduced

* Functions are objects
* `type()`
* `id()`

### Important Observation

```python
type(greet)
```

returns

```python
<class 'function'>
```

---

# Function Analysis: Reassigning Function to Another Variable

### Natural Language

This example stores the same function inside another variable and compares their memory addresses.

### Concepts Introduced

* Multiple references
* Same function object

### Important Observation

Both variables point to the same function object.

Their `id()` values remain identical.

---

# Function: `say_hello()`

### Natural Language

This function simply prints a greeting.

### Concepts Introduced

* Basic function
* Function object creation

---

# Concept: `del say_hello`

### Natural Language

This deletes the variable name that refers to the function.

### Concepts Introduced

* Deleting references
* Namespace management

### Important Observation

`del` removes the function name, **not necessarily the function object**.

If another reference exists, the function still survives.

---

# Function Call After `del`

### Natural Language

This attempts to call a deleted function name.

### Concepts Introduced

* NameError
* Function references

### Important Observation

Python cannot find the deleted name, so it raises

```python
NameError
```

---

# Function Stored Inside a List

### Natural Language

This stores a function together with integers inside a list and later calls it using indexing.

### Concepts Introduced

* Functions inside collections
* Function references
* Calling functions from lists

### Important Observation

Functions behave just like integers, strings, or lists—they are ordinary Python objects.

---

# Function Stored Inside a Set

### Natural Language

This stores a function inside a set and demonstrates that it can still be called.

### Concepts Introduced

* Functions are immutable objects
* Hashable objects
* Functions inside sets

### Important Observation

Function objects can be elements of a set because they are hashable.

---

# Function: `create_greeter(greeting)`

### Natural Language

This function creates and returns another function that remembers the greeting supplied.

### Concepts Introduced

* Returning functions
* Higher-order functions
* Nested functions

### Important Observation

The returned function remembers variables from the outer function.

This behavior is the foundation of **closures**.

---

# Function: `outer_function()` Returning `inner_function`

### Natural Language

This function returns another function, which is later executed independently.

### Concepts Introduced

* Returning functions
* Function references
* Deferred execution

---

# Function: `apply_function(func, value)`

### Natural Language

This function accepts another function and applies it to a given value.

### Concepts Introduced

* Passing functions as arguments
* Higher-order functions

### Important Observation

The same function can work with many different operations.

Example:

```python
apply_function(square,5)

apply_function(cube,5)
```

---

# Function: `square(x)`

### Natural Language

This function returns the square of a number.

### Concepts Introduced

* Simple reusable mathematical function

---

# Function: `cube(x)`

### Natural Language

This function returns the cube of a number.

### Concepts Introduced

* Function reuse
* Passing different functions to one higher-order function

---

# Function: `greet_person(func, name)`

### Natural Language

This function accepts another greeting function and a name, then returns the greeting.

### Concepts Introduced

* Functions as parameters
* Dynamic behavior

---

# Function: `formal_greeting(name)`

### Natural Language

This function returns a formal greeting message.

### Concepts Introduced

* Specialized reusable functions

---

# Function: `casual_greeting(name)`

### Natural Language

This function returns an informal greeting message.

### Concepts Introduced

* Replacing behavior using different functions

---

# Important Patterns Learned

## Pattern 1 — Function Without Return

```python
def greet(name):
    print(name)
```

Returns

```python
None
```

---

## Pattern 2 — Local Scope

```python
def func():
    x = 10
```

---

## Pattern 3 — Global Scope

```python
x = 10

def func():
    print(x)
```

---

## Pattern 4 — Nested Function

```python
def outer():

    def inner():
        pass

    inner()
```

---

## Pattern 5 — Function Assignment

```python
new_function = greet
```

---

## Pattern 6 — Function Stored in List

```python
functions = [greet]
functions[0]()
```

---

## Pattern 7 — Function Returned from Function

```python
def outer():

    def inner():
        pass

    return inner
```

---

## Pattern 8 — Function as Argument

```python
apply(square,5)
```

---

# Common Interview Questions

### What happens in memory when a function is called?

Python creates a new stack frame containing the function's parameters and local variables. The frame is destroyed after the function finishes.

---

### What is the default return value of a function?

```python
None
```

---

### What is Local Scope?

Variables created inside a function.

---

### What is Global Scope?

Variables created outside every function.

---

### What is Enclosing Scope?

Variables belonging to the parent function.

---

### What is Variable Shadowing?

A local variable hides a global variable with the same name.

---

### What is the LEGB Rule?

Python searches variables in this order:

1. Local
2. Enclosing
3. Global
4. Built-in

---

### What are First-Class Functions?

Functions that can be assigned, stored, passed as arguments, and returned from other functions.

---

### Can functions be stored in lists?

Yes.

---

### Can functions be stored in sets?

Yes, because function objects are hashable.

---

### Can one function return another function?

Yes.

---

### Can one function accept another function as an argument?

Yes. Such functions are called **Higher-Order Functions**.

---

# Revision Summary

After completing `3_2_functions.ipynb`, you have learned:

* How Python executes functions in memory
* Function stack frames
* Default return value (`None`)
* Local scope
* Global scope
* Enclosing scope
* Main program scope
* LEGB rule
* Variable shadowing
* Nested functions
* First-class functions
* Function references
* `type()` and `id()` with functions
* Deleting function names using `del`
* Storing functions in lists
* Storing functions in sets
* Returning functions from functions
* Passing functions as arguments
* Higher-order functions
* The foundation of closures
