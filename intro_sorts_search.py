"""
This module is essentially a compilation of basic O(N^2) sorting algorithms and a basic implementation of binary search. I feel like this is a good starting point into algorithms once you have a good understand of linear data structures. This is the first micro-micro project as I make my way through DSA writing code with vim on zsh and VSCode for larger projects.  
"""

"""
You'll notice too that I will mostly write my docs using colloquial language (for aura, although in Python so minus aura, net 0 aura)
"""


def binary_search(arr: list[int], target: int) -> int:
    """
    A lil binary search basic implementation meant for a sorted list of integers.  If yo target int isn't in the list, we return -1. Logarithmic runtime obv
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = ((left + right) // 2)

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


def insertion_sort(arr: list[int]) -> list[int]:
    """
    OG basic sorting alg, stable & O(N^2). Pretty sure this is implemented for smaller lists in  Python's sorted() function, which uses timsort, essentially j insertion then merge sort (i think) for larger lists. Using copy, so 
    """
    n = len(arr)
    for i in range(1, n):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

def selection_sort(arr: list[int]) -> list[int]:
    """
    Basic unstable O(N^2) sorting alg. At each i, the list swaps the min element in the min_index for the element at i. If the element is already in the correct spot for an ascending sort, it will j swap w its own index... who cares dont need to add a check.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr: list[int]) -> list[int]:
    """
    Basic stable O(N^2) sorting alg. Larger elements float to the end of the list like a bubble floats to the top. Peak OG programming methphor we all encouter as beginners (which I am).
    """
    n = len(arr)
    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
           return arr
    return arr

def main():
    """Putting it all together."""
    arr = [10, 2, 32, 1, 2, 75, 1, 0] # Only gna use this test case bc I know this shit works for edge cases. 
     
    print(f"Original Array:  {arr}")
    print(f"Built-in sorted(): {sorted(arr)}")

    # Shallow copies so we don't mutate arr.
    print(f"Insertion Sort:  {insertion_sort(arr[:])}")
    print(f"Selection Sort:  {selection_sort(arr[:])}")
    print(f"Bubble Sort:     {bubble_sort(arr[:])}")

    sorted_arr = sorted(arr)
    target_exists = 32
    target_nonexistent = 127

    print(f"\nBinary Search Results:")

    print(f"Index of {target_exists}: {idx if (idx := binary_search(sorted_arr, target_exists)) != -1 else 'non-existent target'}")
    print(f"Index of {target_nonexistent}: {idx if (idx := binary_search(sorted_arr, target_nonexistent)) != -1 else 'non-existent target'}")

if __name__ == "__main__":
    main()
