"""Utilizing the best of both worlds:
- Insertion sort is faster than merge sort for small array sizes
- Merge sort is way faster than insertion sort as array size grows

Find k such that for an array of size n, subarrays of size k are sorted using insertion sort and then
merged using merge sort"""

from merge_sort import merge
import random


def insertionSort(A, m, n):
    "Insertion sort inside subarray A[m...n]"
    for i in range(m + 1, n + 1):
        x = A[i]
        j = i - 1
        while A[j] > x and j >= m:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x


def mergeInsertionSort(A, p, r, k):
    if p < r:
        q = (p + r) // 2
        if q - p <= k:
            insertionSort(A, p, q)
            insertionSort(A, q + 1, r)
        else:
            mergeInsertionSort(A, p, q, k)
            mergeInsertionSort(A, q + 1, r, k)
        merge(A, p, q, r)


if __name__ == "__main__":
    A = random.sample(range(1000), 100)
    mergeInsertionSort(A, 0, len(A) - 1, k=20)
    print(A)
