```python
# Convert Arithmetic Expression into AST and Three Address Code

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Recursive descent parser
class Parser:
    def __init__(self, expr):
        self.tokens = expr.replace(" ", "")
        self.pos = 0

    def parse(self):
        return self.expression()

    def expression(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in "+-":
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.term()
            node = Node(op, node, right)
        return node

    def term(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in "*/":
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.factor()
            node = Node(op, node, right)
        return node

    def factor(self):
        if self.tokens[self.pos] == "(":
            self.pos += 1
            node = self.expression()
            self.pos += 1
            return node

        start = self.pos
        while self.pos < len(self.tokens) and self.tokens[self.pos].isalnum():
            self.pos += 1
        return Node(self.tokens[start:self.pos])

# Display AST
def display_ast(node, level=0):
    if node:
        print("  " * level + node.value)
        display_ast(node.left, level + 1)
        display_ast(node.right, level + 1)

# Generate Three Address Code
def generate_tac(node, code):
    if node.left is None and node.right is None:
        return node.value

    left = generate_tac(node.left, code)
    right = generate_tac(node.right, code)

    temp = "t" + str(len(code) + 1)
    code.append(f"{temp} = {left} {node.value} {right}")
    return temp

# Main program
expr = input("Enter arithmetic expression: ")

parser = Parser(expr)
ast = parser.parse()

print("\nAbstract Syntax Tree:")
display_ast(ast)

code = []
generate_tac(ast, code)

print("\nThree Address Code:")
for line in code:
    print(line)
```