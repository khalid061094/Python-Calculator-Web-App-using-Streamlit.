def calculate(num1, num2, operation):

    if operation == "Addition (+)":
        return num1 + num2

    elif operation == "Subtraction (-)":
        return num1 - num2

    elif operation == "Multiplication (*)":
        return num1 * num2

    elif operation == "Division (/)":
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2

    elif operation == "Modulus (%)":
        if num2 == 0:
            raise ValueError("Cannot calculate modulus by zero!")
        return num1 % num2

    else:
        raise ValueError("Invalid operation!")
