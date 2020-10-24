# Implementation of Heap Sort in Python

def heapSort(A):
    size=len(A)
    for i in range(int(size/2), -1, -1):
        maxHeapify(A, size, i)


    for i in range((size-1), 0, -1):
        A[i], A[0] = A[0], A[i] # swap as python
        maxHeapify(A, i, 0)

def maxHeapify(A, size, i):
    left = 2*i + 1
    right = 2*i + 2
    if (left<size) and (A[i]<A[left]):
        largest=left
    else:
        largest=i

    if right<size and A[right]>A[largest]:
        largest=right
    if largest != i:
        A[i],A[largest] = A[largest],A[i] # swap
        maxHeapify(A, size, largest)