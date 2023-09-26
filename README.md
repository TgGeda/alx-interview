# Pascal's Triangle Generator

This code is a Python function that generates Pascal's triangle with a given number of rows. Pascal's triangle is a triangular array of binomial coefficients, named after the French mathematician Blaise Pascal. The triangle starts with a single 1 at the top and each subsequent row is created by adding the two numbers above it.

## Function

The function `pascal_triangle(n)` takes an integer `n` as input and returns a list representing Pascal's triangle with `n` number of rows. If `n` is less than or equal to 0, an empty list is returned.

The function follows the following steps to generate the triangle:

1. If `n` is less than or equal to 0, an empty list is returned.
2. The first row of the triangle is initialized with a single element, which is 1.
3. For each row in the triangle (starting from the second row), a new list is created.
4. For each element in the row (excluding the first and last elements), the value is calculated by adding the two elements above it in the previous row.
5. The last element of the row is also 1.
6. The row is added to the triangle.
7. Once all the rows are generated, the triangle is returned.

## Example Usage

The code includes an example usage to demonstrate how to generate Pascal's triangle with 10 rows. 

```python
n = 10
result = pascal_triangle(n)
print(result)
```

This will output the following:

```
[[1],
 [1, 1],
[1, 2, 1],
 [1, 3, 3, 1],
[1, 4, 6, 4, 1],
 [1, 5, 10, 10, 5, 1],
[1, 6, 15, 20, 15, 6, 1],
[1, 7, 21, 35, 35, 21, 7, 1],
 [1, 8, 28, 56, 70, 56, 28, 8, 1],
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
```

The output is a list of lists, where each inner list represents a row in Pascal's triangle.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use and modify it according to your needs.
