# This is the implementation of a quick sort algorithim
# It takes place in O(nlog(n))
def quickSort(array):
    if len(array)<2:
        return array
    pivotElement = array[0]
    maxElements = getMax(array[1:], pivotElement)
    minElements = getMin(array[1:],pivotElement)
    return quickSort(minElements) +[pivotElement] +quickSort(maxElements)
def getMax(array, pivotElement):
    newArray =[]
    for i in array:
        if i>=pivotElement:
            newArray.append(i)
    return newArray

def getMin(array, pivotElement):
    newArray = []
    for i in array:
        if i<pivotElement:
            newArray.append(i)
    return newArray

print(quickSort([3,2,2,4,5]))