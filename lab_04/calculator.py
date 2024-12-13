class Calculator:
    def evaluate(self, rpn_expression):
        stack = []
        for token in rpn_expression.split():
            if token.isnumeric():
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(left / right)
                elif token == '^':
                    stack.append(left ** right)
        return stack[0]

if __name__ == "__main__":
    rpn_expression = "3 4 2 * 1 5 - 2 ^ / +"
    calculator = Calculator()
    result = calculator.evaluate(rpn_expression)
    print(f"Result: {result}")