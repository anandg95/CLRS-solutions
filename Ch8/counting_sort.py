"""Sorting an array of n numbers where every entry is an integer from 0 to k. With this knowledge, it
is possible to sort an array A with 2 passes over it, thereby O(n)
Method:
- Create a counting array C[0...k] that keeps the count of each integer from 0 to k by looping over A once
- Take the cumulative sum inside C so that the number of entries less than or equal to a particular integer is known
- Now scan A from right to left, and place the number in its rightful place in array B using info from C

We loop downwards in step 3 so as to make the sorting 'stable' (Elements with same value appear in the output
array in the same order as they did in the input array)
"""


def couting_sort(A, B, k):
    C = [0] * (k + 1)
    for i in range(len(A)):
        C[A[i]] += 1
    for j in range(1, k + 1):
        C[j] = C[j] + C[j - 1]

    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]  # -1 since list indexing starts at 0
        C[A[i]] -= 1


if __name__ == "__main__":
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    k = 5
    B = [None] * len(A)
    couting_sort(A, B, k)
    print(B)
