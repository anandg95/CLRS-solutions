"""
Quicksort is an inplace divide and conquer sorting algorithm. On a subarray A[p...r], it works by:
- Splitting the range p...r as p...q-1, q, q+1...r using a PARTITION algorithm
- After the subarray is partitioned about q, it has the following property:
    * A[i] <= A[q] in range p...q-1
    * A[i] > A[q] in range q+1...r
- A[q] is known as the pivot using which the subarray is partitioned
- Now quicksort is applied recursively in the left and right subarrays, A[p...q-1] and A[q+1...r]
- After A[p...q-1] and A[q+1...r] are sorted, there is no need to combine as A[p...r] will become sorted automatically
"""

import random


def partition(A, p, r):
    x = A[r]  # pivot
    i = p - 1  # less than pivot elements counter
    for j in range(p, r):
        # search for items less than pivot
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    # place the pivot in after the last element from search, ie, i+1
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1  # q


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


if __name__ == "__main__":
    A = random.sample(range(100), 20)
    print(A)
    quick_sort(A, 0, len(A) - 1)
    print(A)
