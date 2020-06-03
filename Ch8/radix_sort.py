"""Radix sort sorts numbers using digits - it compares digits of same significance over all elements to sort
in that 'bucket'. It starts by sorting based on all least significant digits, then sorting with the second least
signficant digit, finally getting to the most significant digit. Counting sort is used to sort digits. In case 2
digits are equal, we want the numbers to retain the same order, hence the need for a stable sort. Radix sort
is useful for sorting dates, by sorting based on date first, then month and finally year"""


def counting_sort(A, divisor):
    C = [0] * 10  # 0...9
    B = [0] * len(A)

    for e in A:
        num = e // divisor
        C[num % 10] += 1
    for j in range(1, 10):
        C[j] += C[j - 1]

    for i in range(len(A) - 1, -1, -1):
        digit = (A[i] // divisor) % 10
        B[C[digit] - 1] = A[i]
        C[digit] -= 1

    # copy back
    for j in range(len(A)):
        A[j] = B[j]


def radix_sort(A):
    i = 0
    largest = max(A)
    divisor = 1
    while largest // divisor > 0:
        counting_sort(A, divisor)
        divisor *= 10


if __name__ == "__main__":
    A = [329, 457, 657, 839, 436, 720, 355, 1050, 2, 15]
    radix_sort(A)
    print(A)
