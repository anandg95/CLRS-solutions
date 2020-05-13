"""
Finding the subarray whose sum is maximum, and returns the start index, end index and the sum.
For an array that contains only positive numbers, the solution is trivial and the maximum subarray
is the whole array itself. The problem becomes interesting where there are both negative and positive numbers
in an array.
Example: [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
Returns --> (low=7, high=10, sum=43)

Solving using the divide and conquer method:

Divide:
- For any subproblem A[low...high] split the subarray into A[low...mid] and A[mid+1...high]

Conquer:
- The maximum subarray for the subarray could be in:
   * the left sub subarray A[low...mid]
   * the right sub subarray A[mid+1...high]
   * Cross the midpoint from i to j such that low <= i <= mid < j <= high
- 1 and 2 can be solved recursively. 3 is O(n) algorithm that is solved separately called maximum_crossing_sub_array

Combine:
- The maximum subarray has to be the maximum of these 3 thereby solving the subproblem
"""
from math import inf


def maximum_crossing_sub_array(A, low, mid, high):
    """
    The possible maximum subarray that contains the midpoint
    Starts from mid and goes in either direction till the edges and the maximum sum is noted for left and right
    """
    left_sum = right_sum = -inf

    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def maximum_sub_array(A, low, high):
    if low == high:  # base case
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = maximum_sub_array(A, low, mid)
        right_low, right_high, right_sum = maximum_sub_array(A, mid + 1, high)
        cross_low, cross_high, cross_sum = maximum_crossing_sub_array(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low, high, sum = maximum_sub_array(A, 0, len(A) - 1)
    print(low, high, sum)
