# Implementation of Bubble Sort in Python

def bubbleSort(array):
    n = len(array)
	
    # Going through all array elements
    for i in range(n-1):
        # Last i elements already in place, so we subtract from total
        for j in range(0, n-i-1):
            # If prior element is greater than the next one, we swap them
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

