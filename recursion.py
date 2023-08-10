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