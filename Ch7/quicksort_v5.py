"""Tail recursive quicksort to reduce the number of recursive calls.
Ensure that the worst case stack depth is theta(lg n). How do we ensure smallest stack size? Make sure the smaller
subarray is passed recursively and the larger is solved in the loop"""

from quicksort import partition


def tail_recursive_quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        l_size = q - p
        r_size = r - q
        if l_size < r_size:
            tail_recursive_quicksort(A, p, q - 1)
            p = q + 1  # larger is from A[q+1...r], hence p = q+1
        else:
            tail_recursive_quicksort(A, q + 1, r)
            r = q - 1  # larger is from A[p...q-1], hence r = q-1


if __name__ == "__main__":
    from random import sample

    A = sample(list(range(100)), 20)
    print(A)
    tail_recursive_quicksort(A, 0, len(A) - 1)
    print(A)
