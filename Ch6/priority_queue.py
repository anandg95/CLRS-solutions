"Priority queue using MaxHeap - Priority of an element at index i in A is A[i], also known as key"

from heap_sort import MaxHeap, max_heapify, build_max_heap
from math import ceil


def maximum(S):
    "Returns element with maximum key - O(1)"
    return S[0]


def extract_max(S):
    "Remove and return the element of S with largest key - O(lg n)"
    if S.heap_size < 1:
        raise Exception("Trivial heap")
    max, S[0] = S[0], S[S.heap_size - 1]
    S.heap_size -= 1
    max_heapify(S, 0)
    return max


def insert(S, k):
    "Insert element with key k to S - O(lg n)"
    S.heap_size += 1
    S.append(-float("inf"))
    increase_key(S, S.heap_size - 1, k)


def increase_key(S, i, k):
    "Increases the value of element i's key to new value k. Assumes that k is at least as large as A[i]. O(lg n)"

    def parent(i):
        return ceil(i / 2) - 1

    if k < S[i]:
        raise Exception("New key is smaller than current key")
    S[i] = k
    # Preserve max heap property by checking recursively along the parent path, ie, sift upwards
    while i > 0 and S[parent(i)] < S[i]:
        S[i], S[parent(i)] = S[parent(i)], S[i]
        i = parent(i)


def delete(S, i):
    """
    Deletes the item at node i. Delete is done in 2 steps:
    1. Increase the element at i to infinity using increase_key(). This bring S[i] to the root of the max heap.
    2. Replace the root with the last leaf in the heap. Decrement heap size by 1 and apply max_heapify()
    This fixes the gap that is left in the subtree where S[i] is the root - O(lg n)
    """
    increase_key(S, i, float("inf"))
    S[0] = S[S.heap_size - 1]
    S.heap_size -= 1
    max_heapify(S, 0)
