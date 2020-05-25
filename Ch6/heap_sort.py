"""
Properties of a heap:
- Assuming index in the array representation of a heap start at 1, if the index of parent is i, the index of 
  left and right children would be 2i and 2i+1 respectively. Conversely, the parent of node i will be floor(i/2)
- To convert a heap in binary tree form to array form, traverse the tree horizontally
- If the total number of elements is n, then indices from floor(n/2) + 1...n are all leaves
- The height of a heap - Number of edges in the longest path from root to any node. It is equal to floor(lg n)
- Number of nodes in a complete binary heap of height h = 2^(h+1) - 1
- For a max heap, a parent node would be larger than both its children and vice versa for a min heap
- **There are at most ceil(n/2^(h+1)) nodes of height h in any n-element binary heap. Leaves are at height=0 and 
  root height=h

Heap Sort:
- BUILD-MAX-HEAP in place from the unsorted array A - O(n)
- The root would be the largest element in the heap - swap that with A[-1] and decrement heap size by 1.
  Largest element is now at the very end of the array
- Perform MAX-HEAPIFY on A[1] to recover the max-heap property. Recursively swap A[1] with element at A[heap_size]
  till completely sorted. MAX-HEAPIFY is recursive and is O(lg n)

Overall complexity:
O(n) + O(n*lg n) = O(nlg n)

Advantageous over merge sort in that sorting is done in-place
"""
import random


class MaxHeap(list):
    def __init__(self, A):
        list.__init__(self, A)
        self.heap_size = len(A)


def max_heapify(A, i):
    "Max heapify the subtree with index i as root"
    left_child_index = 2 * i + 1  # indices start at 0
    right_child_index = 2 * i + 2
    largest = i
    if left_child_index < A.heap_size and A[left_child_index] > A[i]:
        largest = left_child_index
    if right_child_index < A.heap_size and A[right_child_index] > A[largest]:
        largest = right_child_index
    if i != largest:
        # swap i with largest and fix the child node just modified
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    "Create a max heap representation for a given array"
    for i in range(A.heap_size // 2 - 1, -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    build_max_heap(A)
    print(A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        A.heap_size -= 1
        max_heapify(A, 0)


if __name__ == "__main__":
    A = MaxHeap(random.sample(range(100), 20))
    heap_sort(A)
    print(A)
