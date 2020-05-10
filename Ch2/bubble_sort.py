import random


def bubbleSort(A):
    L = len(A)
    for i in range(L - 1):
        for j in range(L - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


if __name__ == "__main__":
    A = random.sample(range(100), 20)
    bubbleSort(A)
    print(A)
