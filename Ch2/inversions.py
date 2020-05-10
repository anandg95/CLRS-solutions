"""Inversion Count for an array indicates – how far (or close) the array is from being sorted.
If array is already sorted then inversion count is 0. If array is sorted in reverse order that
inversion count is the maximum.
This is counting the number of inversions using merge sort
Counting the number of inversions using the merge step:
- There is a Left subarray and Right subarray which are sorted per se
- If all elements of the right subarray are larger than all elements of the left subarray then
  there are no inversions
- If any element `x` of the L subarray is larger than any element `y` of the R subarray,
  then consequently all elements to the right of `x` are larger than `y`
"""

import random


def merge(A, p, q, r):
    "A[p...q] is a sorted subarray, A[q+1...r] is also a sorted subarray"
    i = j = 0  # subarray counters
    k = p  # main array counter
    n1 = q - p + 1
    n2 = r - q
    n_inversions = 0

    L = A[p : q + 1]
    R = A[q + 1 : r + 1]

    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:  # element of L subarray larger than element of R subarray
            A[k] = R[j]
            j += 1
            n_inversions += len(L[i:])
        k += 1

    if i < n1:
        A[k : r + 1] = L[i:]
    return n_inversions


def mergeSort(A, p, r):
    n_inversions = 0
    if p < r:
        q = (p + r) // 2
        n_inversions += mergeSort(A, p, q)
        n_inversions += mergeSort(A, q + 1, r)
        n_inversions += merge(A, p, q, r)
    return n_inversions


if __name__ == "__main__":
    A = list(range(20, 0, -1))
    # for a set of descending natual numbers n to 1, the number of inversions = n(n-1)/2, here 190
    print(mergeSort(A, 0, len(A) - 1))
