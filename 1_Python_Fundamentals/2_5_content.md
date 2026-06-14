# 2.1 fundamentals file content:

1. The print() Function: Covers how the sep parameter defaults to a space (' ') and how end defaults to a newline character ('\n'), and how to override them to customize output formatting.

2. Data Types: Breakdowns of all 9 fundamental data types showcased in your notebook:

Basic: int, float, bool, str, and complex.

Collections: list, tuple, set, and dict.

3. The type() Function: A reminder of how to check any value's class classification dynamically.


# 2.2 fyndamentals file content:

### Stylish/Advanced Initialization Ways:

1. Multiple Assignments in One Line: Assigning unique values to multiple variables simultaneously.

2. Chained Assignment: Assigning the same value to multiple variables in a single stroke.

### Comments in Python:

Comments are ignored by the interpreter and are used to document code.

1. Single-Line Comments: Created using the # symbol.

2. Multi-Line Comments: Created using triple quotes (\"\"\" \"\"\" or ''' ''').

### Core Definitions: Compilation, Keywords & Identifiers:

1. Compilation: The process of converting high-level source code into binary language (machine-readable code) so the computer can execute it.

2. Keywords: Special reserved words that help the compiler or interpreter translate high-level code into machine code.

   Python contains 35 keywords (referenced as 32 traditionally in some notes, but keyword.kwlist exposes the full list).

   Examples include: False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield.

3. Identifiers: User-defined names given to programmable elements within code like variables, functions, classes, etc.

### Mandatory Rules for Creating Identifiers:

1. No Leading Digits: An identifier cannot start with a number, symbol, or special character (e.g., 1name is invalid), but digits can be used at the end (e.g., name1).

2. Allowed Characters: Only alphanumeric characters and underscores (_) are allowed. The underscore is the only valid special character.

3. No Keywords: A reserved keyword cannot be used as an identifier name (e.g., you cannot name a variable def or if).

### Typing vs. Binding:

A simple mental framework to differentiate the two:

1. Typing: Refers to the container (What kind of data is stored?).

2. Binding: Refers to the action or method (Assigning/connecting that data to a variable).

### Static vs. Dynamic Paradigms:

1. Binding (Static vs. Dynamic)

   Static Binding: The computer knows exactly which instruction to use beforehand, and that connection remains completely fixed and unaltered while the program runs.

     Real-life analogy: Saving your dad's phone number as Dad -> 9876543210. The name and connection are permanently fixed; no choice or decision has to be evaluated during runtime.

   Dynamic Binding: A variable can be freely connected to entirely different values during program execution, and Python dynamically evaluates the connection at runtime

2. Typing (Static vs. Dynamic)

   Static Typing (e.g., Java): Once a variable is declared with a specific data type, its data type is permanently locked and cannot change later.

     Example (Java): int x = 10; x = "Hello"; triggers a compilation error because an integer variable cannot morph into a string container.

   Dynamic Typing (e.g., Python): A variable is never permanently tied to one static data type. It can dynamically hold entirely different types of values over time as the code executes.


