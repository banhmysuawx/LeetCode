
from re import A


def Partition(arr, start, end):
    pivot = arr[0]
    i = 1
    for j in range(1, len(arr)):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[0], arr[i - 1] = arr[i - 1], arr[0]
    return i - 1

def QuickSort(arr, start, end):
    if start < end:
        pivot = Partition(arr, start, end)
        QuickSort(arr, start, pivot - 1)
        QuickSort(arr, pivot + 1, end)
    return arr

arr = [5, 2, 4, 6, 1, 3]
print(QuickSort(arr, 0, len(arr) - 1))

def bubbleSort(arr):
    swaped = False
    for n in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaped = True
        if not swaped:
            break 
arr = [5, 2, 4, 6, 1, 3]  
bubbleSort(arr)
print(arr)

def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
# print(arr)
arr = [5, 2, 4, 6, 1, 3]
insertSort(arr)
print(arr)

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min] , arr[i]

arr = [5, 2, 4, 6, 1, 3]
selectionSort(arr)
print(arr)