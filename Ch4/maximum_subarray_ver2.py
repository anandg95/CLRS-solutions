"""
The maximum subarray problem in linear time (Kadane's algorithm)
Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Working:
- This algorithm does not allow the maximum subarray to be negative. If so, it returns zero
- Scan an array from left to right keeping track of 2 sums:
    * best Sum - which is the maximum subarray sum
    * current sum - Sum till the current element being scanned in the array. If upon adding the current
      element, the sum becomes negative, the sum is reset to zero, and the low index for holding current
      sum is moved to that position
    If current_sum exceeds best sum, we assign best sum as current sum
"""


def maximum_sub_array_kadane(A):
    best_sum = float("-inf")
    current_sum = 0

    best_start = best_end = 0
    current_start = 0

    for current_end in range(len(A)):
        current_sum += A[current_end]
        if current_sum < 0:
            current_sum = 0
            current_start = current_end + 1  # reset to next position

        if current_sum > best_sum:
            best_sum = current_sum
            best_end = current_end
            best_start = current_start

    return (best_start, best_end, best_sum)
    # includes start and end indices therefore A[best_start:best_end+1] are the elements


if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(maximum_sub_array_kadane(A))
