#heap sort
#Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. 
#The algorithm can be divided into two main phases: building a max heap from the input data and then repeatedly extracting the maximum element from the heap and rebuilding the heap until it is empty.
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    #max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    #Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

set_data = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52,
            87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

print("Heap Sort:", heap_sort(set_data.copy()))

#All sorting algorithms
#Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

#timing function
import time

def time_sort(sort_func, data):
    start = time.time()
    sort_func(data.copy())
    end = time.time()
    return end - start

#Load the datasets
import pandas as pd

temps = pd.read_csv(r"C:\Users\DELL 5520\Downloads\temperatures_auckland_data.csv")
kiwi = pd.read_csv(r"C:\Users\DELL 5520\Downloads\kiwi_data.csv")

#temperature data
tmax = temps["Tmax"].dropna().tolist()
tmin = temps["Tmin"].dropna().tolist()

#kiwi data
weight = kiwi["Weight(kg)"].dropna().tolist()
height = kiwi["Height(cm)"].dropna().tolist()

#all algorithms sorting the datasets
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

for name, func in algorithms.items():
    print(f"{name}: {time_sort(func, tmax):.6f} seconds")
    print(f"{name}: {time_sort(func, tmin):.6f} seconds")

#checking the current working directory to ensure the CSV files are in the correct location
import os
print(os.getcwd())

