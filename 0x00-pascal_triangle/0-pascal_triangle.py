#!/usr/bin/python3
<<<<<<< HEAD
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
=======


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle up to n.
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


if __name__ == "__main__":
    print(pascal_triangle(5))
>>>>>>> a9655a69dfa8fdf589afbf3f0329d114ac716545
