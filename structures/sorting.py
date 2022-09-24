# quicksort, mergesort e bucket sor
from typing import List, Union
def mergeSort(arr: List[Union[int,str,float]]):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    L = arr[:mid]
    R = arr[mid:]

    L = mergeSort(L)
    R = mergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    return arr


def insertionSort(arr):

    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > up:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = up
    return arr

def bucketSort(arr, slot_num=10):

    max_ele = max(arr)
    min_ele = min(arr)
    rnge = (max_ele - min_ele)/slot_num
    buckets = [[] for _ in range(slot_num)]


    for ele in arr:
        diff = (ele - min_ele) / rnge - int((ele - min_ele) / rnge)
        if diff == 0 and ele != min_ele:
            buckets[int((ele - min_ele) / rnge) - 1].append(ele)
        else:
            buckets[int((ele - min_ele) / rnge)].append(ele)

    for i in range(slot_num):
        if len(buckets[i]) != 0:
            buckets[i] = insertionSort(buckets[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(buckets[i])):
            arr[k] = arr[i][j]

    return arr



        

def printList(arr):
    print("[", end=' ')
    for ele in arr:
        print(ele, end=' ')
    print("]")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    print("------ Merge Sort ------")
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

    arr = [12, 11, 13, 5, 6, 7]

    print("------ Quick Sort ------")
    print("Given array is", end="\n")
    printList(arr)
    arr = quickSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

