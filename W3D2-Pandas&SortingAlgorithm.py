#What is pip?
#Pip is a package manager for Python. It allows you to install and manage additional libraries and dependencies that are not included in the standard Python library. 
#What it does
#You can easily install packages from the Python Package Index (PyPI) and keep them up to date. It is a powerful tool for managing your Python environment and ensuring that you have the necessary packages for your projects.

#What is pandas?
#Pandas is a powerful and widely-used open-source data analysis and manipulation library for Python. 
#It provides data structures and functions needed to work with structured data seamlessly.

#Selection sort
#Selection sort is a simple comparison-based sorting algorithm. It works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the first unsorted element until the entire list is sorted.

#Selection sort function
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
                arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
                
#set data list
set_data = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

#sort data list
sorted_data = selection_sort(set_data)
print("Sorted data:", sorted_data)

#merge sort
#Merge sort is a divide-and-conquer algorithm that breaks down a list into smaller sublists until each sublist contains a single element. 
#Then, it merges those sublists back together in a sorted order to produce the final sorted list.

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

print(merge_sort(set_data.copy()))

#quick sort
#Quick sort is a highly efficient sorting algorithm that uses a divide-and-conquer approach. 
#It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
#The sub-arrays are then sorted recursively.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(set_data.copy()))

#csv files
import pandas as pd

temps = pd.read_csv("temperatures_auckland_data.csv")
kiwi = pd.read_csv("kiwi_data.csv")

#temp data
print(temps.sort_values("Tmax"))
print(temps.sort_values("Tmin"))

#kiwi data
print(kiwi.sort_values("Weight(kg)"))
print(kiwi.sort_values("Height(cm)"))

