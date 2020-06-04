"""
Bucket sort:
Assuming the entries in an array are drawn from a uniform distribution in [0,1], it is possible to sort
the array in O(n) time using bucket sort. To sort A[1...n], we do:
- Create n equally sized sub-intervals/buckets in the range [0,1]. 
- Place each array element in its appropriate bucket
- Sort each bucket
- Expand the buckets sequentially to obtain the sorted list

Complexity of Bucket sort:
- Overall running time is the time to scan once through A and place every element in the rightful bucket +
  the sum of times for sorting individual buckets using selection sort
    T(n) = 0(n) + Σ O(ni^2) where ni is the number of elements in bucket i
- Expected run time E[T(n)] = 0(n) + Σ O(E[ni^2])
- Since elements are drawn from a uniform distribution and assigned to `n` uniformly spaced buckets, each element 
  has an equal probability of being in each bucket, independent of each other.

- Prob of element being assigned to bucket i, p = 1/n
  Prob of otherwise, q = 1 - 1/n
  Number of trials, n = n (n numbers to be placed in various buckets)
  
- Therefore the number of elements in bucket i follows a binomial distribution with given p and q.
  E[ni] = np = 1
  var[ni] = npq = 1 - 1/n
  var[X] = E[X^2] - E[X]^2
  Therefore, E[ni^2] = var[ni] + E[ni]^2 = 2 - 1/n

- Expected runtime, E[T(n)] = 0(n) + Σ (2-1/n) = 0(n)
"""

from itertools import chain
import random
import sys

sys.path.append("../")
from Ch2.insertion_sort import insertion_sort


def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for e in A:
        bucket_index = int(n * e)
        B[bucket_index].append(e)
    analyse(B, n)
    for bucket in B:
        insertion_sort(bucket)
    return list(chain(*B))


def analyse(B, n):
    n_items_per_bucket = [len(bucket) for bucket in B]
    # since buckets are identical, we can take individual buckets as independent samples of the population
    sample_size = n // 2  # computing mean over all samples would be trivial
    mean = sum(random.sample(n_items_per_bucket, sample_size)) / sample_size
    var = sum([(mean - n) ** 2 for n in n_items_per_bucket]) / n
    print(f"Experimental mean : {mean}")
    print(f"Experimental variance: {var}")
    print(f"Theoretical mean : 1")
    print(f"Theoretical variance : {1-1/n}")


if __name__ == "__main__":
    A = [random.random() for _ in range(10000)]
    # print(A)
    B = bucket_sort(A)
    # print(B)
