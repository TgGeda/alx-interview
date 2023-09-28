#!/usr/bin/python3 

def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal Triangle of n.
    Returns an empty list if n <= 0.
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    triangle.append([1])  # First row of Pascal Triangle
    
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        
        for j in range(len(triangle[i - 1]) - 1):
            curr_row = triangle[i - 1]
            row.append(curr_row[j] + curr_row[j + 1])  # Calculate each element of the row
        
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    
    return triangle


