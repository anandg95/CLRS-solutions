"Same as quicksort, but chooses random pivot in PARTITION"

from quicksort import partition
import random


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


if __name__ == "__main__":
    A = random.sample(range(100), 20)
    print(A)
    quicksort(A, 0, len(A) - 1)
    print(A)
