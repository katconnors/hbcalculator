"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    summation = num1 + num2
    return summation


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    subtraction = num1 - num2
    return subtraction


def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    multi = num1 * num2
    return multi


def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    dividen = num1 / num2
    return dividen


def square(num1):
    """Return the square of num1."""
    squared = num1*num1
    return squared

def cube(num1):
    """Return the cube of num1."""
    cube_result = num1 ** 3
    return cube_result


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    powered = num1**num2
    return powered 

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    modified = num1%num2
    return modified