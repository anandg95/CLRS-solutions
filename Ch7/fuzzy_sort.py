"""
Sort a list of intervals (as opposed to a set of numbers) using quicksort. Problem statement:
- Every list element i is [ai, bi] where ai <= bi
- Find permutation <i1, i2, ...in> such that there exists cj belonging to [aij, bij] satisfying c1 <= c2 <=...cn
Comparing two intervals:
- i > j if [ai, bi] is disjoint from [aj, bj] and ai < bi
- i = j if [ai, bi] intersection [aj, bj] not equals null
We will be stealing the idea from quicksort_v3
"""
import random
from dataclasses import dataclass


def partition(A, p, r):
    pivot = random.randint(p, r)
    A[p], A[pivot] = A[pivot], A[p]
    q = p
    t = p
    a, b = A[p]
    for j in range(p + 1, r + 1):
        if A[j][1] < a:  # stritly less than
            A[j], A[q] = A[q], A[j]
            A[j], A[t + 1] = A[t + 1], A[j]
            q = q + 1
            t = t + 1
        elif A[j][1] >= a and A[j][0] <= b:  # intersects
            # A intersect B != 0 and B intersect C != 0 does not imply A intersect C != 0
            # Hence update intersection
            a, b = max(a, A[j][0]), min(b, A[j][1])
            t = t + 1
            A[j], A[t] = A[t], A[j]
    return q, t


def quicksort(A, p, r):
    if p < r:
        q, t = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, t + 1, r)


if __name__ == "__main__":
    A = [(2, 4), (0, 1), (3, 5), (-1, -2), (0, 99)]
    quicksort(A, 0, len(A) - 1)
    print(A)
