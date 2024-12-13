class Converter:
    def __init__(self):
        self.stack = []
        self.output = []

    def precedence(self, op):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedences.get(op, 0)

    def to_rpn(self, expression):
        for token in expression:
            if token.isnumeric():
                self.output.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  
            else:
                while self.stack and self.precedence(token) <= self.precedence(self.stack[-1]):
                    self.output.append(self.stack.pop())
                self.stack.append(token)
        
        while self.stack:
            self.output.append(self.stack.pop())

        return ' '.join(self.output)

if __name__ == "__main__":
    expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2".split()
    converter = Converter()
    rpn_expression = converter.to_rpn(expression)
    print(f"RPN: {rpn_expression}")
