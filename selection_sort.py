# Selection Sort Algorithim is used to sort an array in O(n^2)

def findSmallest(array):
    smallestIndex = 0
    smallestValue = array[smallestIndex]
    # This determines the smallest element in the current array and returns the index
    for i in range(len(array)):
        if array[i]<smallestValue:
            smallestValue = array[i]
            smallestIndex = i
    return smallestIndex

def selection_sort(array):
    toSort = array
    sortedArray = []
    for i in range(len(array)):
        # This traverses the array and run the findSmallest function for every member of the Array
        smallestIndex = findSmallest(toSort)
        sortedArray.append(toSort.pop(smallestIndex))
        
    return sortedArray




print(selection_sort([4,2,3,2,5]))