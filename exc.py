
#using split function to split user input according to space
#using map to convert each string to integer after splitting
ARRAY = list(map(int, input("Enter list of integers (0s and 1s): ").split()))

#create function to returns the lenght of the longest subarray
def longest_subarray(ARRAY):
    COUNT_ZERO = 0
    COUNT_ONE = 0
    LIST=[]
    RESULT=0
      #if integer is 0 then add it to count zero otherwise add it to ones
    for num in ARRAY:
        if num == 0:
           COUNT_ZERO += 1
           
        else:
            COUNT_ONE += 1
           
             # compare the counters and the smaller will be taken to returns the longest subarray
        if COUNT_ZERO>COUNT_ONE:
                LIST=COUNT_ONE
        else:
                LIST=COUNT_ZERO
            
            
        RESULT = LIST*[1]+LIST*[0]

    return RESULT

print(longest_subarray(ARRAY))