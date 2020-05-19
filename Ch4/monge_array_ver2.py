"""
Same as monge_array.py but avoiding copying odd and even indices rows into 2 new arrays.
So, instead of passing a list, we will be passing the indices of the initial array in subsequent
recursions using a a range object. This gets rid of additional memory overhead
"""

from monge_array import find_min


def odd_from_even(A, odd_indices, f_even):
    f = []
    n_odd = len(odd_indices)
    for i, index in enumerate(odd_indices):
        f.append(f_even[i])

        row = A[index]
        left = f_even[i]
        if i == len(f_even) - 1 and len(f_even) == n_odd:
            right = len(row) - 1
        else:
            right = f_even[i + 1]

        minimum_pos = find_min(row, left, right)
        f.append(minimum_pos)

    if n_odd < len(f_even):
        f.append(f_even[-1])
    return f


def leftmost_minimum_index(A, indices, power):
    if len(indices) == 1:
        row0 = A[indices[0]]
        return [find_min(row0, 0, len(row0) - 1)]

    even_indices = range(0, len(A), 2 ** power)
    odd_indices = range(2 ** (power - 1), len(A), 2 ** power)

    f_even = leftmost_minimum_index(A, even_indices, power + 1)
    indices = odd_from_even(A, odd_indices, f_even)
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
    print(leftmost_minimum_index(A, range(len(A)), power=1))
