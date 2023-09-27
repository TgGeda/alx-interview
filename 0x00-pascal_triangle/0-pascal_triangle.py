#!/usr/bin/python3
# This function generates a Pascal's triangle with n number of rows
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    """
    triangle = []

    if n > 0:
        for i in range(1, n + 1):
            row = []
            coefficient = 1

            for j in range(1, i + 1):
                row.append(coefficient)
                coefficient = coefficient * (i - j) // j

            triangle.append(row)

    return triangle


# Example usage
n = 10
result = pascal_triangle(n)
print(result)
