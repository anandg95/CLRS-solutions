"""Merge sort works recursively in the following manner:
    - Split a subarray from A[p...r] into A[p...q] and A[q+1...r]
    - Sort the 2 smaller arrys
    - Merge the 2 sorted subarrays to create a sorted subarray in A[p...r]
"""

import math
import random


def merge(A, p, q, r):
    "A[p...q] is a sorted subarray, A[q+1...r] is also a sorted subarray"
    i = j = 0  # subarray counters
    k = p  # main array counter
    n1 = q - p + 1
    n2 = r - q

    L = A[p : q + 1]
    R = A[q + 1 : r + 1]

    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    if i < n1:
        A[k : r + 1] = L[i:]
    # it is not mandatory to fill in the rest of the right subarray
    # This is because sorting is done in-place. Elements of the right subarray are essentially stored in the
    # right half (q+1...r+1) of the subarray in A.


def mergeSort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


if __name__ == "__main__":
    A = random.sample(range(100), 20)
    print(A)
    mergeSort(A, 0, len(A) - 1)
    print(A)
