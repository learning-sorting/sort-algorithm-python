arr = [4, 12, 6, 23, 43, 12, 9, 0]

def insertionSort(arr):
  for i in range(len(arr)):
    temp = arr[i]
    j = i
    while (j>0 and temp < arr[j-1]):
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = temp
  return arr


print(insertionSort(arr))
