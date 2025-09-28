# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    :param num1: First number (float)
    :param num2: Second number (float)
    :param operation: One of ['add', 'subtract', 'multiply', 'divide']
    :return: Result of operation or an error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
