#Bubble Sort
#Bubble Sort is a simple comparison-based sorting algorithm. 
#It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
#Its called "bubble sort" as the smaller elements "bubble" to the front of the list, while larger ones move to the end.

#how they work
#Start at the beginning of the list
#Compare item i with item i+1
#Swap if they're in the wrong order
#Repeat for the entire list
#Keep repeating passes until no swaps occur

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

#Insertion Sort
#Insertion Sort is a simple comparison-based sorting algorithm that builds the sorted array one item at a time.
#It works by repeatedly taking the next unsorted item and inserting it into the correct position in the already sorted portion of the array.
#how they work
#Assume the first element is sorted
#Take the next element
#Compare it backwards through the sorted portion
#Shift elements to the right
#Insert the element in the correct position

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

#given data
set_data = [
67, 12, 89, 43, 56, 34, 78, 23, 91, 45,
18, 76, 39, 52, 87, 65, 29, 83, 16, 72,
47, 54, 31, 95, 68, 21, 84, 59, 13, 75
]

#printing sorted data
print(bubble_sort(set_data.copy()))
print(insertion_sort(set_data.copy()))

#Timing Function
import time

def time_sort(sort_function, data):
    start = time.time()
    sort_function(data.copy())
    end = time.time()
    return end - start

#Datasets for testing
datasets = [
    [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
     890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
     432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
     765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
     908, 765, 432, 789, 123, 890, 567, 876, 345, 654],

    [456, 234, 765, 321, 908, 567, 876, 345, 654, 432,
     789, 123, 890, 567, 876, 345, 654, 321, 908, 765,
     432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
     765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
     908, 765, 432, 789, 123, 890, 567, 876, 345, 654],

    ["apple", "banana", "orange", "grape", "kiwi", "pineapple",
     "mango", "peach", "pear", "watermelon", "strawberry",
     "blueberry", "raspberry", "blackberry", "lemon", "lime"]
]

#Running timed comparisons
for i, dataset in enumerate(datasets, start=1):
    bubble_time = time_sort(bubble_sort, dataset)
    insertion_time = time_sort(insertion_sort, dataset)

    print(f"Dataset {i}")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds\n")

