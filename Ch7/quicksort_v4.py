"""
Quicksort using Hoare partition. For A[p...r], 
- Set pivot as A[p]
- Find inversions and swap them
- one loop counter variable will scan top down, other scans bottom up
- When the variables cross each other, it is time to stop
"""


def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= x:
                break
        while True:
            i = i + 1
            if A[i] >= x:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            # crossover. pivot is at j now
            return j


def quick_sort(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


if __name__ == "__main__":
    A = [13, 19, 9, 5, 12, 8, 7, 4, 13, 2, 6, 21]
    quick_sort(A, 0, len(A) - 1)
    print(A)
