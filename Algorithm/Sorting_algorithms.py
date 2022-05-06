# selection sort
def selectionsort(array):
    for i in range(len(array)):
        min_idx = i
        for idx in range(i+1, len(array)):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


# insertion sort
def insertionsort(array):
    for i in range(len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array

import math

# shell sort
def shellsort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[i - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1

    return array


# heap sort
def heapify(array, n, i):
    largest = i
    l = 2 * i +1
    r = 2 * i +2
    