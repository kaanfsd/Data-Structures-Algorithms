def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    
    first = 0
    last = len(list) - 1
    
    while (first <= last):
        # Floor division (//) is rounds down to the nearest whole number
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

def verify(index):
    """
    Verifies the given index is not None and prints the result.
    """
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")
             
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 8)
verify(result)
