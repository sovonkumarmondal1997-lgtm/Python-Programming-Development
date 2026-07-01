# Python Functions Notes (Part 5)

# File Name

## `3_5_functions.ipynb`

---

# Important Concepts Covered

This notebook introduces three important built-in **Higher-Order Functions** used extensively in Python programming and data processing:

* `map()`
* `filter()`
* `reduce()`

It also explains how these functions work together with:

* Lambda functions
* User-defined functions
* Iterables
* Functional programming

---

# Functional Programming

## What is Functional Programming?

Functional programming is a programming style where functions are treated as first-class objects and computations are performed by applying functions to data.

Instead of modifying data directly, functional programming focuses on creating new transformed results.

### Characteristics

* Uses reusable functions
* Avoids unnecessary loops
* Reduces code duplication
* Produces cleaner and shorter code
* Encourages immutable data

---

# Built-in Higher-Order Function: `map()`

## What is `map()`?

`map()` applies the same function to every element of an iterable and returns a new iterator.

### Syntax

```python
map(function, iterable)
```

---

## Function: `square(number)`

### Natural Language

This helper function returns the square of a given number.

### Concepts Introduced

* Helper function
* Mathematical transformation
* Passing functions into `map()`

---

## Function: Applying `map(square, numbers)`

### Natural Language

This applies the `square()` function to every element in the list and returns the squared values.

### Concepts Introduced

* `map()`
* Function as argument
* Data transformation

### Important Observation

The original list remains unchanged.

---

## Function: Using Lambda with `map()`

```python
map(lambda x: x ** 2, numbers)
```

### Natural Language

This squares every number using a lambda function instead of a separately defined helper function.

### Concepts Introduced

* Lambda with `map()`
* Anonymous functions
* Concise functional programming

---

# Built-in Higher-Order Function: `filter()`

## What is `filter()`?

`filter()` selects only those elements that satisfy a given condition.

### Syntax

```python
filter(function, iterable)
```

---

## Difference Between `map()` and `filter()`

| map()                                     | filter()                                         |
| ----------------------------------------- | ------------------------------------------------ |
| Transforms every element                  | Selects only matching elements                   |
| Number of outputs equals number of inputs | Output size may be smaller                       |
| Returns modified values                   | Returns original values satisfying the condition |

---

## Function: `is_even(number)`

### Natural Language

This helper function checks whether a number is even.

### Concepts Introduced

* Boolean return values
* Conditional logic
* Predicate functions

### Important Observation

A function used with `filter()` should normally return either:

* `True`
* `False`

---

## Function: Applying `filter(is_even, numbers)`

### Natural Language

This filters the list and returns only the even numbers.

### Concepts Introduced

* Filtering data
* Boolean conditions
* Higher-Order Function

---

## Function: Using Lambda with `filter()`

```python
filter(lambda x: x % 2 == 0, numbers)
```

### Natural Language

This filters even numbers using a lambda function.

### Concepts Introduced

* Lambda expression
* Anonymous predicate
* Functional programming

---

# Built-in Higher-Order Function: `reduce()`

## What is `reduce()`?

`reduce()` repeatedly combines elements of an iterable into a single final value.

Unlike `map()` and `filter()`, `reduce()` is not a built-in function.

It must be imported.

```python
from functools import reduce
```

---

## Syntax

```python
reduce(function, iterable)
```

---

## Function: `add(x, y)`

### Natural Language

This helper function returns the sum of two numbers.

### Concepts Introduced

* Binary function
* Aggregation
* Accumulation

---

## Function: Applying `reduce(add, numbers)`

### Natural Language

This repeatedly adds two numbers until one final sum remains.

### Concepts Introduced

* Aggregation
* Running total
* Higher-Order Function

### Execution Example

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

Final Result

```python
15
```

---

## Function: Using Lambda with `reduce()`

```python
reduce(lambda x, y: x + y, numbers)
```

### Natural Language

This calculates the total sum using an anonymous function.

### Concepts Introduced

* Lambda
* Aggregation
* Functional programming

---

## Function: Multiplication Using `reduce()`

```python
reduce(lambda x, y: x * y, numbers)
```

### Natural Language

This multiplies all numbers together and returns the final product.

### Concepts Introduced

* Running product
* Aggregation
* Functional programming

---

# Comparison of `map()`, `filter()`, and `reduce()`

| Function   | Purpose                       | Output                         |
| ---------- | ----------------------------- | ------------------------------ |
| `map()`    | Transform every element       | Iterable of transformed values |
| `filter()` | Select matching elements      | Iterable of filtered values    |
| `reduce()` | Combine all elements into one | Single value                   |

---

# Real-World Applications

## `map()`

Used when every record requires the same transformation.

Examples

* Convert Celsius to Fahrenheit
* Convert names to uppercase
* Calculate salaries after increment
* Square numbers

---

## `filter()`

Used when only selected records are needed.

Examples

* Active customers
* Employees above a salary threshold
* Even numbers
* Passed students

---

## `reduce()`

Used for aggregation.

Examples

* Total sales
* Sum of marks
* Product of values
* Maximum value
* Minimum value

---

# Important Patterns Learned

## Pattern 1 — `map()`

```python
list(map(function, iterable))
```

---

## Pattern 2 — Lambda with `map()`

```python
list(map(lambda x: x ** 2, numbers))
```

---

## Pattern 3 — `filter()`

```python
list(filter(function, iterable))
```

---

## Pattern 4 — Lambda with `filter()`

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

---

## Pattern 5 — Importing `reduce()`

```python
from functools import reduce
```

---

## Pattern 6 — `reduce()`

```python
reduce(function, iterable)
```

---

## Pattern 7 — Lambda with `reduce()`

```python
reduce(lambda x, y: x + y, numbers)
```

---

# Common Mistakes

### Mistake 1

Forgetting to import `reduce()`.

```python
from functools import reduce
```

---

### Mistake 2

Expecting `filter()` to modify values.

`filter()` only selects elements.

---

### Mistake 3

Using a helper function with `filter()` that does not return `True` or `False`.

---

### Mistake 4

Forgetting to convert `map()` and `filter()` results into lists.

```python
list(map(...))
list(filter(...))
```

---

### Mistake 5

Confusing `map()` with `reduce()`.

`map()` transforms every element.

`reduce()` combines all elements into one result.

---

# Best Practices

* Use `map()` for transformations.
* Use `filter()` for selecting data.
* Use `reduce()` for aggregation.
* Prefer lambda functions only for simple expressions.
* Use helper functions for complex logic.
* Keep functions pure whenever possible.

---

# Interview Questions

### What is functional programming?

A programming style that solves problems by applying functions to data while emphasizing reusable and independent functions.

---

### What does `map()` do?

It applies a function to every element of an iterable.

---

### What does `filter()` do?

It returns only the elements that satisfy a condition.

---

### What does `reduce()` do?

It repeatedly combines elements into a single final value.

---

### Which module contains `reduce()`?

```python
functools
```

---

### Why does `filter()` require a Boolean-returning function?

Because it decides whether each element should be kept (`True`) or discarded (`False`).

---

### Which function is used for aggregation?

`reduce()`

---

### Which function changes every element?

`map()`

---

### Which function selects matching records?

`filter()`

---

# Revision Summary

After completing `3_5_functions.ipynb`, you have learned:

* Functional programming basics
* Higher-order functions in practice
* `map()` for transforming data
* `filter()` for selecting data
* `reduce()` for aggregating data
* Using lambda functions with all three
* Helper functions with higher-order functions
* Data transformation
* Data filtering
* Data aggregation
* Differences between `map()`, `filter()`, and `reduce()`
* Common mistakes and best practices for functional programming in Python
