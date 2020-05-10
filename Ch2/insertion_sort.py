import random


def insertion_sort(a: list):
    """Insertion sort works by taking an element from the unsorted subarray and placing it into the 
    rightful spot in the sorted subarray. Start off with the first element in the list as being the sorted
    subarray. Now preogressively take elements from the unsorted section until we hit the end of the array"""

    L = len(a)
    for i in range(1, L):
        x = a[i]
        j = i - 1
        while a[j] > x and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


if __name__ == "__main__":
    a = random.sample(range(1, 100), 20)
    print(f"Unsorted version: {a}")
    insertion_sort(a)
    print(f"Sorted version {a}")
