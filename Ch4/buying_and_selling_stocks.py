"""
This is an application of the maximum subarray problem.

Problem: Suppose A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
represents the price of stocks each day. Find the days at which one should buy and sell so as to
maximize profit. In this case stocks must be bought on 7th day (63) and sold on the 11th day (106)
(days counted from 0) creating a profit of 43.

This could be simply explained as finding two indices i, j such that j >= i and A[j] - A[i] = maximum
Running all combinations is an O(n^2) algorithm.

Alternative:
- Create an array storing the diffs of adjacent elements of A such that diff[i] =  - A[i] + A[i+1]
- Difference between any 2 indices i and j of A can be computed as a running sum of diff[i...(j-1)]
    sum(diff[i...(j-1)]) = (- A[i] + A[i+1]) + (-A[i+1] + A[i+2]) + .... + (- A[j-1] + A[j])
                         = A[j] - A[i]
- So the problem of stocks has reduced to the maximum subarray problem of the difference array
- Total complexity:
    * For determining the difference array : O(n)
    * maximum subarray problem : O(nlgn)
    Total complexity = O(n) + O(nlgn) = O(nlgn), better than cominations 
"""

from maximum_subarray import maximum_sub_array


def smart_stocks(stocks):
    A = [stocks[i] - stocks[i - 1] for i in range(1, len(stocks))]
    i, j, profit = maximum_sub_array(A, 0, len(A) - 1)
    print(f"Buy at day {i}, sell at day {j+1} for a profit of {profit}")


stocks = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
smart_stocks(stocks)
