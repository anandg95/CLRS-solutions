"""
An array A[1...n] contains all the integers from 0 to n except one.It would be easy to determine the
missing integer in O(n) time by using an auxiliary array B[0...n] to record which numbers appear in A.
In this problem, however, we cannot access an entire integer in A with a single operation. The elements
of A are represented in binary, and the only operation we can use to access them is "fetch the jth bit 
of A[i]," which takes constant time.
Show that if we use only this operation, we can still determine the missing integer in O(n) time.
"""


def missing(A, lsb):
    if len(A) == 0:
        return 0
    num_one = num_zero = 0
    A_zero = []
    A_one = []

    for i in A:
        if i[-1 - lsb] == "0":
            num_zero += 1
            A_zero.append(i)
        else:
            num_one += 1
            A_one.append(i)

    if num_one >= num_zero:
        return 2 * missing(A=A_zero, lsb=lsb + 1)
    else:
        return 2 * missing(A=A_one, lsb=lsb + 1) + 1


if __name__ == "__main__":
    from random import randint, shuffle
    from math import log, floor

    N = 100
    n_bits = floor(log(N, 2)) + 1

    A_int = list(range(N))
    missing_integer = A_int.pop(randint(0, N - 1))
    A = [bin(i).split("0b")[1].zfill(n_bits) for i in A_int]
    shuffle(A)

    print(f"Array: {A}")
    print(f"Element popped: {missing_integer}")
    print(f"Element discovered: {missing(A, lsb=0)}")
