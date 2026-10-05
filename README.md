# Arithmetic Expression to AST and Three Address Code

## 📌 Description

This Python program converts an arithmetic expression into:

1. **Abstract Syntax Tree (AST)**
2. **Three Address Code (TAC)**

The program uses a **Recursive Descent Parser** to analyze the arithmetic expression while maintaining operator precedence.

It supports the basic arithmetic operators:

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

It also supports **parentheses** for controlling the order of evaluation.

---

## 🛠️ Technologies Used

- **Python 3**
- Recursive Descent Parsing
- Abstract Syntax Tree (AST)
- Three Address Code (TAC)

---

## 📂 Program Structure

```text
.
├── Program.py
└── README.md
```

---

## ⚙️ How It Works

### 1. Node Class

The `Node` class represents a node in the Abstract Syntax Tree.

Each node contains:

- `value` – operator or operand
- `left` – left child
- `right` – right child

Example:

```text
      +
     / \
    a   b
```

Here, `+` is the parent node and `a` and `b` are its children.

---

### 2. Recursive Descent Parser

The parser breaks the arithmetic expression into different levels:

```text
Expression
    ↓
  Term
    ↓
 Factor
```

The grammar used is approximately:

```text
Expression → Term { (+ | -) Term }

Term → Factor { (* | /) Factor }

Factor → Operand | (Expression)

Operand → Alphanumeric characters
```

This structure ensures that multiplication and division have higher precedence than addition and subtraction.

---

### 3. Abstract Syntax Tree

After parsing, the expression is represented as an AST.

For example:

```text
a + b * c
```

produces:

```text
+
├── a
└── *
    ├── b
    └── c
```

This correctly represents the precedence of `*` over `+`.

---

### 4. Three Address Code

The program then traverses the AST and generates Three Address Code using temporary variables.

For:

```text
a + b * c
```

the TAC is:

```text
t1 = b * c
t2 = a + t1
```

Each instruction contains at most one operation and uses a temporary variable to store intermediate results.

---

## ▶️ How to Run

### Step 1: Check Python

Make sure Python 3 is installed.

```bash
python --version
```

### Step 2: Run the Program

```bash
python Program.py
```

### Step 3: Enter an Expression

Example:

```text
Enter arithmetic expression: a+b*c
```

---

## 💻 Example

### Input

```text
a+b*c
```

### Output

```text
Abstract Syntax Tree:
+
  a
  *
    b
    c

Three Address Code:
t1 = b * c
t2 = a + t1
```

---

## 🧪 Another Example

### Input

```text
(a+b)*c
```

### Output

```text
Abstract Syntax Tree:
*
  +
    a
    b
  c

Three Address Code:
t1 = a + b
t2 = t1 * c
```

---

## ✨ Features

- Converts arithmetic expressions into an AST.
- Generates Three Address Code automatically.
- Uses recursive descent parsing.
- Handles operator precedence.
- Supports parentheses.
- Uses temporary variables for intermediate calculations.
- Simple and easy-to-understand implementation for Compiler Design Lab.

---

## ⚠️ Limitations

The current implementation:

- Supports only `+`, `-`, `*`, and `/`.
- Does not support exponentiation (`^`).
- Does not handle unary operators such as `-a`.
- Does not provide detailed syntax-error messages.
- Operands are limited to alphanumeric characters.
- The parser assumes that the entered expression is valid.

---

## 🎯 Applications

This program demonstrates important concepts used in **Compiler Design**, including:

- Lexical representation of expressions
- Recursive descent parsing
- Abstract Syntax Trees
- Operator precedence
- Intermediate Code Generation
- Three Address Code

These concepts are commonly used during the **syntax analysis** and **intermediate code generation** phases of a compiler.

---

## 📚 Compiler Design Concepts

```text
Arithmetic Expression
        ↓
Recursive Descent Parser
        ↓
Abstract Syntax Tree (AST)
        ↓
Tree Traversal
        ↓
Three Address Code (TAC)
```

---

## 👨‍💻 Author

**Soutik**

Compiler Design Lab Project
