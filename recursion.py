# Recursion are functions that calls each other
# They have a base case and a recursive case
# The function keeps a stack of each recursive tasks in memory stack and pops
# off each layer of the stack to complete the execution.


# This function counts down recursively
def recursion(n):
    # This is the base case
    # It makes sure that we only print positive integers
    if(n<1):
        return 
    else:
        #  This is the recursive case. It recursively counts down on the value of n
        print(n)
        recursion(n-1)


# Test call for the recursive function
recursion(5)

# A recursive function for sum of array
def sum_of_array(array):
    if len(array)>1:
        return array.pop() + sum_of_array(array)
    else:
        return array[0]

print(sum_of_array([2,3,4]))    

# A recursive function for 
def noOfElements(array):
    if len(array)!=0:
        array.pop()
        return 1+noOfElements(array)
    else:
        return 0
print(noOfElements([1,2,3,4,5]))

def maxNumber(array):
    
    if len(array)==1:
        return array[0]
    else:
        max = maxNumber(array[1:])
        if array[0]>max:
            return array[0]
        else:
            return max
print(maxNumber([1,2,7,4,5]))
    
    

