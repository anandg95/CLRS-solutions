"""
Quicksort has a worst case running time of O(n^2) if all the elements in the array are equal.
Modify the partition algorithm so that there are 2 points of partition, q and t such that:
- All of A[p...q-1] <= A[q]
- All of A[q...t] are equal
- All of A[t+1...r] > A[q]
In such a case, an array with all equal elements will be sorted in 1 call to PARTITION
"""


def partition(A, p, r):
    x = A[r]  # pivot
    A[p], A[r] = A[r], A[p]  # bring pivot to front
    i = p  # low pos of pivot stream
    k = p  # high pos of pivot stream (inclusive)

    for j in range(p + 1, r + 1):
        if A[j] < x:
            # element at j ought to at the low index of pivot stream. Pop the pivot from low and put it a high+1
            # element originally ay high+1, put it at j
            A[j], A[i] = A[i], A[j]
            A[k + 1], A[j] = A[j], A[k + 1]
            # change the positions
            i = i + 1
            k = k + 1
        elif A[j] == x:
            k = k + 1
            A[j], A[k] = A[k], A[j]
    return i, k  # q, t


def quick_sort(A, p, r):
    if p < r:
        q, t = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, t + 1, r)


if __name__ == "__main__":
    A = [7, 5, 3, 2, 6, 7, 9, 4, 5, 1, 2, 4, 7]
    quick_sort(A, 0, len(A) - 1)
    print(A)
