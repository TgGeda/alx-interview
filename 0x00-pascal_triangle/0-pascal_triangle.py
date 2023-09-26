#!/usr/bin/python3
# This function generates a Pascal's triangle with n number of rows
def pascal_triangle(n):
    # If n is less than or equal to 0, an empty list is returned
    if n <= 0:
        return []

    # The first row of the triangle is initialized with 1
    triangle = [[1]]
    
    # For each row in the triangle, a list is created
    for i in range(1, n):
        row = [1]
        # For each element in the row, the value is calculated by adding the two elements above it in the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # The last element of the row is also 1
        row.append(1)
        # The row is added to the triangle
        triangle.append(row)
    
    # The generated triangle is returned
    return triangle

# Example usage
n = 10
result = pascal_triangle(n)
print(result)
