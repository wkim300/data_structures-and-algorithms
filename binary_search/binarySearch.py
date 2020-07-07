"""[summary]
Binary Search implementation in Python

Resource: https://www.geeksforgeeks.org/binary-search/
"""

def binary_search_iter(arr, x):
    """[summary]
    Iterative version of binary search
    Returns the index of x in the array; else return -1
    Args:
        arr ([python list]): search space
        x ([value]): item to search for in the arr
    """
    low = 0 
    hi = len(arr) - 1 
    while low <= hi:
        mid = (low + hi)//2  # calculate mid
        if arr[mid] == x:
            return mid
        # x is on the left side
        elif x < arr[mid]:
            hi = mid - 1
        # x is on the right side
        elif arr[mid] < x:
            low = mid + 1
    return -1  # x is not found

def binary_search_recur(arr, low, hi, x):
    """[summary]
    Recursive version of binary search
    Returns the index of x in the array; else return -1
    Args:
        arr ([python list]): search space
        low ([int]): low index
        hi ([int]): high index
        x ([value]): item to search for in the arr
    """
    if hi < low:
        return -1

    mid = (low + hi)//2
    if arr[mid] == x:
        return mid
    # x is on the left side
    if x < arr[mid]: 
        return binary_search_recur(arr, low, mid-1, x)
    # x is on the right side
    if x > arr[mid]: 
        return binary_search_recur(arr, mid+1, hi, x)
    

if __name__ == "__main__":
    # Driver Code 
    arr = [ 2, 3, 4, 10, 40, 60 ] 
    print("Testing iterative case...")
    for x in arr:
        res = binary_search_iter(arr, x)
        print(f"Searching x = {x}, Found item = {arr[res]} at index = {res}")

    arr = [ 2, 3, 4, 10, 40, 60 ] 
    print("\nTesting recursive case...")
    for x in arr:
        res = binary_search_recur(arr, 0, len(arr)-1, x)
        print(f"Searching x = {x}, Found item = {arr[res]} at index = {res}")
    # Invalid search
    x=50
    res = binary_search_recur(arr, 0, len(arr)-1, x)
    if res != -1:
        print(f"Searching x = {x}, Found item = {arr[res]} at index = {res}")
    else:
        print(f"x = {x} not found...")