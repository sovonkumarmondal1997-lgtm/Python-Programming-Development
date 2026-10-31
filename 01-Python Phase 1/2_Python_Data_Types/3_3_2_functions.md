# Python Functions Notes (Part 3)

# File Name

## `3_3_functions.ipynb`

---

# Important Concepts Covered

This notebook introduces **Lambda Functions (Anonymous Functions)** and demonstrates how they can be used to write short, concise functions and integrate with Python's built-in functions.

Topics covered:

* Benefits of functions
* Lambda functions
* Anonymous functions
* Lambda syntax
* Single-expression functions
* Lambda with multiple arguments
* Lambda with one argument
* Using lambda with `map()`
* Using lambda with `sorted()`
* `key` parameter in sorting

---

# Benefits of Using Python Functions

Functions are one of the most important building blocks in Python.

## 1. Code Reusability

Write code once and use it many times.

---

## 2. Modularity

Break a large program into smaller manageable pieces.

---

## 3. Readability

Programs become easier to understand.

---

## 4. Easier Debugging

Errors can be isolated inside individual functions.

---

## 5. Maintainability

Updating one function automatically improves every place where it is used.

---

## 6. Reduced Code Duplication

Avoid writing the same logic repeatedly.

---

# Lambda Functions

## What is a Lambda Function?

A **lambda function** is a small anonymous function created using the `lambda` keyword.

Unlike normal functions created with `def`, lambda functions:

* do not have a function name
* usually contain only one expression
* automatically return the result of that expression

---

## Syntax

```python
lambda parameters: expression
```

Example

```python
lambda x: x * 2
```

---

# Difference Between `def` and `lambda`

| def Function                    | Lambda Function             |
| ------------------------------- | --------------------------- |
| Has a name                      | Usually anonymous           |
| Can contain multiple statements | Only one expression         |
| Uses `return`                   | Returns automatically       |
| Better for complex logic        | Better for short operations |

---

# Function Analysis

---

## Function: Lambda Function That Adds Two Numbers

```python
add = lambda x, y: x + y
```

### Natural Language

This lambda function accepts two numbers and returns their sum.

### Concepts Introduced

* Lambda syntax
* Multiple parameters
* Automatic return value
* Anonymous function

### Important Observation

The expression after `:` is automatically returned.

No `return` keyword is required.

---

## Function: Lambda Function That Squares a Number

```python
square = lambda x: x ** 2
```

### Natural Language

This lambda function accepts one number and returns its square.

### Concepts Introduced

* Single parameter
* Mathematical expression
* Anonymous function

### Important Observation

A lambda function can contain only one expression.

---

## Function: Using Lambda with `map()`

```python
numbers = [1,2,3,4,5]

squared_numbers = list(
    map(lambda x: x**2, numbers)
)
```

### Natural Language

This applies the lambda function to every element in the list and creates a new list of squared values.

### Concepts Introduced

* `map()`
* Applying a function to every element
* Functional programming
* Converting `map` object into a list

### Important Observation

`map()` does not modify the original list.

It creates an iterator that is converted into a list using `list()`.

---

# Built-in Function: `map()`

## What is `map()`?

`map()` applies a function to every element of an iterable.

### Syntax

```python
map(function, iterable)
```

Example

```python
map(lambda x:x*2, numbers)
```

---

## When Should `map()` Be Used?

Use `map()` when the same operation must be applied to every element of a collection.

---

# Function: Sorting Students Using Lambda

```python
students_sorted = sorted(
    students,
    key=lambda student: student[1]
)
```

### Natural Language

This sorts the student list according to the second element (age) of each tuple.

### Concepts Introduced

* `sorted()`
* `key`
* Lambda as sorting key
* Tuple indexing

### Important Observation

Without the `key`, Python sorts tuples using the first element.

The `key` allows custom sorting.

---

# Built-in Function: `sorted()`

## What is `sorted()`?

Returns a new sorted collection without modifying the original collection.

---

## Syntax

```python
sorted(iterable)
```

or

```python
sorted(iterable, key=function)
```

---

## The `key` Parameter

The `key` tells Python **what value should be used for comparison while sorting**.

Example

```python
key=lambda student: student[1]
```

Python compares only the age.

---

# Function: Lambda Function That Doubles a Number

```python
double = lambda x: x * 2
```

### Natural Language

This lambda function multiplies the input value by two.

### Concepts Introduced

* Basic lambda function
* Returning computed values
* Function assignment

### Important Observation

A lambda function behaves exactly like a normal function after being assigned to a variable.

---

# Normal Function vs Lambda

Normal Function

```python
def double(x):
    return x * 2
```

Equivalent Lambda

```python
double = lambda x: x * 2
```

Both produce the same result.

The only difference is the syntax.

---

# Important Patterns Learned

## Pattern 1 — Basic Lambda

```python
lambda x: x * 2
```

---

## Pattern 2 — Multiple Parameters

```python
lambda x, y: x + y
```

---

## Pattern 3 — Assigning Lambda

```python
square = lambda x: x ** 2
```

---

## Pattern 4 — Lambda with `map()`

```python
map(lambda x: x ** 2, numbers)
```

---

## Pattern 5 — Lambda with `sorted()`

```python
sorted(data, key=lambda x: x[1])
```

---

## Pattern 6 — Tuple Indexing Inside Lambda

```python
lambda student: student[1]
```

---

# Common Mistakes

### Mistake 1

Trying to write multiple statements inside a lambda.

❌ Invalid

```python
lambda x:
    y = x + 1
    return y
```

Reason:

A lambda function can contain only one expression.

---

### Mistake 2

Using lambda for large programs.

Large logic should always be written using `def`.

---

### Mistake 3

Forgetting to convert `map()` into a list.

```python
list(map(...))
```

---

### Mistake 4

Confusing `sorted()` with `.sort()`.

* `sorted()` returns a new collection.
* `.sort()` modifies the original list.

---

# Best Practices

* Use lambda only for short functions.
* Prefer `def` for complex business logic.
* Use meaningful variable names.
* Use lambda mainly with:

  * `map()`
  * `filter()`
  * `sorted()`
  * `min()`
  * `max()`

---

# Interview Questions

### What is a lambda function?

A small anonymous function consisting of a single expression.

---

### Why is it called an anonymous function?

Because it normally has no function name.

---

### Can a lambda function contain multiple statements?

No.

It can contain only one expression.

---

### Does a lambda function require `return`?

No.

The expression is automatically returned.

---

### When should lambda be used?

For small, simple functions used only once or passed to another function.

---

### Can lambda have multiple parameters?

Yes.

Example

```python
lambda x, y: x + y
```

---

### What does `map()` do?

It applies a function to every element of an iterable.

---

### Why use `list(map(...))`?

Because `map()` returns a map object (iterator), which is converted into a list for easier use.

---

### What is the purpose of the `key` parameter in `sorted()`?

It specifies the value used for comparing elements during sorting.

---

# Revision Summary

After completing `3_3_functions.ipynb`, you have learned:

* Benefits of functions
* Lambda (anonymous) functions
* Lambda syntax
* Difference between `def` and `lambda`
* Automatic return behavior
* Single-parameter lambda
* Multi-parameter lambda
* Function assignment
* Using lambda with `map()`
* Applying operations to every element
* Using lambda with `sorted()`
* The `key` parameter for custom sorting
* Tuple indexing inside lambda expressions
* Best practices and common mistakes when using lambda functions
