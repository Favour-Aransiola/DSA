# The Binary Search is an algorithim for finding
# a value from a list of sorted values in O(log n).
# It returns the index of the element if found or None if not.

def binary_search(array, search_item):
    # The function takes in the array to sort and the item to search for.
    low = 0 # this is initially set to the index of the first value of the array
    high = len(array)-1 # this is initially set to the last value of the array

    while low<=high: # this is used to find out if the first index is greater than the last index for the search
        mid = (low+high)//2 # this calculates the midpoint of the array
        guess = array[mid]
        if(search_item==guess):
            return mid # confirms if the value in the middle iis the search value.
        if(guess<search_item):
            low = mid +1 # checks if our guess is less than the search item, adjusts the low index
        else:
            high = mid-1 # # checks if our guess is greater than than the search item, adjusts the high index
    return None # The search item is not found
print(binary_search([1,2,3,4,5,6,7,8],5)) # Used to test, should return 4

