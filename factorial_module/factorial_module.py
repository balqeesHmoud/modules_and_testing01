def factorial_iterative(n):
    """Calculate the factorial of a positive integer using iterative approach."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursion(n):
    """Calculate the factorial of a positive integer using recursion."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n - 1)


def clumsy(n):
    if n < 0:
        raise ValueError("Clumsy factorial is undefined for negative numbers.")
    if n == 0:
        return 0

    operations = ['*', '/', '+', '-']
    result = n
    idx = 0
    for i in range(n - 1, 0, -1):
        op = operations[idx % 4]
        if op == '*':
            result *= i
        elif op == '/':
            result //= i  # floor division
        elif op == '+':
            result += i
        elif op == '-':
            result -= i
        idx += 1

    return result


