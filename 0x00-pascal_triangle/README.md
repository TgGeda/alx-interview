# Pascal Triangle

This code implements a function that generates the Pascal triangle. The Pascal triangle is a triangular array of numbers in which each number is the sum of the two numbers directly above it. The function takes an integer `n` as input and returns a list of lists representing the Pascal triangle with `n` rows.

## Usage

```python
triangle = pascal_triangle(n)
```

- `n` (int): The number of rows in the Pascal triangle.

## Function Description

### `pascal_triangle(n)`

This function takes an integer `n` as input and returns a list of lists representing the Pascal triangle.

#### Parameters

- `n` (int): The number of rows in the Pascal triangle.

#### Returns

- `triangle` (list): A list of lists representing the Pascal triangle.

## Implementation Details

1. If `n` is less than or equal to 0, an empty list is returned.
2. The Pascal triangle is initialized with zeros.
3. For each row `i` from 0 to `n-1`:
   - A new row is created and filled with zeros.
   - The first and last indices of the new row are set to 1.
   - The values for the current row are calculated based on the previous row.
   - The calculated row is added to the Pascal triangle.
4. The Pascal triangle is returned.

## Example

```python
>>> triangle = pascal_triangle(5)
>>> print(triangle)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

In the above example, the function `pascal_triangle(5)` returns a Pascal triangle with 5 rows.
