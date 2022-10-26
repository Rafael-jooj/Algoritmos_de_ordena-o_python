## Bubble Sort
# def bubble(array):

#     for final in range(len(array), 0, -1):
#         exchanging = False

#         for current in range(0, final - 1):
#             if array[current] > array[current + 1]:
#                 array[current + 1], array[current] = array[current], array[current + 1]
#                 exchanging = True

#         if not exchanging:
#             break

## Selection Sort
def selection_sort(array):
    cont = 0
    cont2 = 0
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            cont2 += 1
            if array[right] < array[min_index]:
                min_index = right
                cont +=1

        array[index], array[min_index] = array[min_index], array[index]
    print(cont)
    print(cont2)
    print('-----------')

## Insertion Sort
# def insertion(array):
#     for p in range(0, len(array)):
#         current_element = array[p]

#         while p > 0 and array[p - 1] > current_element:
#             array[p] = array[p - 1]
#             p -= 1

#         array[p] = current_element

## Merge Sort
def sort(array):
    sort_half(array, 0, len(array) - 1)


def sort_half(array, start, end):
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, start, middle)
    sort_half(array, middle + 1, end)

    merge_sort(array, start, end)


def merge_sort(array, start, end):
    array[start: end + 1] = sorted(array[start: end + 1])

## Quick Sort

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

## Couting Sort

def countingSort(arr):
    size = len(arr)
    output = [0] * size

    # count array initialization
    count = [0] * 10

    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]

## Heap Sort

def heapify(arr, n, i):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Build max heap
    for i in range(n//2, -1, -1):
      heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapify root element
        heapify(arr, i, 0)

## Radix Code

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):


    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10



import matplotlib.pyplot as plt
import time
qt = 2
arquivos=[]
tempo=[]
while qt <= 10:
    crescente = [int(a) for a in open(f'arquivos/{qt}-crescente.txt').read().split('\n') if a != '']
    tempo_inicio = time.time()
    sort(crescente)
    t = round((time.time() - tempo_inicio), 3)
    tempo.append(t)
    arquivos.append(str(qt))
    qt *= 2

print(tempo)
plt.plot(arquivos, tempo)
# plt.show()    