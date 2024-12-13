from converter import Converter
from calculator import Calculator

def main():
    expression = input("Enter a mathematical expression: ").split()
    converter = Converter()
    rpn_expression = converter.to_rpn(expression)
    print(f"RPN: {rpn_expression}")

    calculator = Calculator()
    result = calculator.evaluate(rpn_expression)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
