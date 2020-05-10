import random
from math import floor


def binarySearch(A, item, low, high):
    if low < high:
        mid = floor((low + high) / 2)
        if item == A[mid]:
            return mid
        if item > A[mid]:
            return binarySearch(A, item, mid + 1, high)
        else:
            return binarySearch(A, item, low, mid)


if __name__ == "__main__":
    A = list(range(1000000))  # 1 mil
    item = 691574
    print(binarySearch(A, item, 0, len(A) - 1))
