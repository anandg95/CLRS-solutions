"""
Whenever we pick two rows and two columns of a Monge array and consider the four elements at the 
intersections of the rows and the columns, the sum of the upper-left and lower-right elements is less 
or equal to the sum of the lower-left and upper-right elements.

Finding the leftmost minimum element in each row in a monge array:
- If f(i) is the index of the column containing the leftmost minimum element of row i, then f(1) <= f(2) <= f(3) ...
- Here is a description of a divide-and-conquer algorithm that computes the left-most minimum element in
  each row of an m × n Monge array A. Construct a submatrix A′ of A consisting of the even-numbered
  rows of A. Recursively determine the leftmost minimum for each row of A′. Then compute the leftmost minimum
  in the odd-numbered rows of A. Explain how to compute the leftmost minimum in the odd-numbered rows
  of A (given that the leftmost minimum of the even-numbered rows is known) in O(m + n) time.

  Qualitatively:
    Given point 1, for odd number row 2i + 1, f(2i) <= f(2i+1) <= f(2i+2)
                                      2i + 3, f(2i+2) <= f(2i+3) <= f(2i+5)
    We see that the boundaries intersect for every pair of adjacent odd numbers.
    Every odd row need be checked between its boundaries. There are m/2 odd number rows.
    With n columns to scan over and m/2 number of columns repeting, total running time would be of the
    order of n + m/2.
    Hence the complexity for determining the odd rows leftmost minimum is O(n + m), given the leftmost
    minimum of even rows are known.
- Once the even rows are separated, again divide it into odd and even rows. This process continues.
- The total complexity of the algorithm is O(m + n log m) by divide and conquer
"""


def odd_from_even(A_odd, f_even):
    f = []
    m = len(A_odd[0])
    for i, row in enumerate(A_odd):
        f.append(f_even[i])  # even first

        left = f_even[i]  # boundaries for A_odd[i]
        if i == len(f_even) - 1 and len(f_even) == len(A_odd):
            # equal number of even and odd rows
            right = m - 1
        else:
            # one even row more than odd rows
            right = f_even[i + 1]

        # find the leftmost minimum for the odd row
        minimum = row[left]
        minimum_pos = left
        for j in range(left, right + 1):
            if row[j] < minimum:
                minimum, minimum_pos = row[j], j
        f.append(minimum_pos)
    if len(A_odd) < len(f_even):  # one even row more than odd rows
        f.append(f_even[-1])
    return f


def leftmost_minimum_index(A):
    if len(A) == 1:
        # base case, the 0th row [[1,2,3,...]]
        minimum = float("inf")
        minimum_pos = -1
        for i, element in enumerate(A[0]):
            if element < minimum:
                minimum_pos, minimum = i, element
        return [minimum_pos]

    A_even = A[::2]  # This is a copy :(
    A_odd = A[1::2]  # same here
    even_indices = leftmost_minimum_index(A_even)
    indices = odd_from_even(A_odd, even_indices)
    return indices


if __name__ == "__main__":
    A = [
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7],
        [45, 44, 32, 37, 23],
        [36, 33, 19, 21, 6],
        [75, 66, 51, 53, 34],
    ]
    print(leftmost_minimum_index(A))
