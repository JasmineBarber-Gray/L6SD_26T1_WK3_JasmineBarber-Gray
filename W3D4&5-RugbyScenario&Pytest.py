
#Rugby Players Data import
import pandas as pd

df = pd.read_excel(r"C:\Users\DELL 5520\Downloads\rugby_players_data-1.xlsx")

print(df.head())
print(df.columns)

ages = df["Age"].dropna().tolist()

#Sorting algorithms
#1. Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#2. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#3. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

#Helper function for merge sort
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

#5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#6. Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

#Main function for heap sort
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

#Testing timer
import time

def time_sort(func, data):
    start = time.perf_counter()
    func(data.copy())
    end = time.perf_counter()
    return end - start

#Comparing algorithms and saving results
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

#Storing results in a dictionary
results = {}

#prints the results dictionary to verify it's being populated correctly
print(results)
#Rugby Players Data import
import pandas as pd

df = pd.read_excel(r"C:\Users\DELL 5520\Downloads\rugby_players_data-1.xlsx")

print(df.head())
print(df.columns)

ages = df["Age"].dropna().tolist()

#Sorting algorithms
#1. Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#2. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#3. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

#Helper function for merge sort
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

#5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#6. Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

#Main function for heap sort
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

#Testing timer
import time

def time_sort(func, data):
    start = time.perf_counter()
    func(data.copy())
    end = time.perf_counter()
    return end - start

#Comparing algorithms and saving results
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

#Storing results in a dictionary
results = {}

# Comparing algorithms
results = {}

for name, func in algorithms.items():
    #time the sorting functions
    time_taken = time_sort(func, ages)
    #store the sorted data in a variable for verification
    sorted_data = func(ages.copy())
    #Store the result in the dictionary
    results[name] = time_taken
    
    #Print the time result for each algorithm
    print(f"{name}: {time_taken:.6f} seconds")
    
    print("First 15 Sorted Data:", sorted_data[:15])  # Print the sorted data for verification

# Save to Excel
results_df = pd.DataFrame(list(results.items()), columns=["Algorithm", "Time (seconds)"])
results_df.to_excel("Time_Complexities.xlsx", index=False)

print("Results saved to Time_Complexities.xlsx")

complexity_data = {
    "Algorithm": ["Bubble", "Insertion", "Selection", "Merge", "Quick", "Heap"],
    "Sorted": ["O(n)", "O(n)", "O(n²)", "O(n log n)", "O(n log n)", "O(n log n)"],
    "Unsorted": ["O(n²)", "O(n²)", "O(n²)", "O(n log n)", "O(n log n)", "O(n log n)"],
    "Duplicate": ["O(n²)", "O(n²)", "O(n²)", "O(n log n)", "O(n log n)", "O(n log n)"],
    "Reverse": ["O(n²)", "O(n²)", "O(n²)", "O(n log n)", "O(n²)", "O(n log n)"],
    "No Data": ["O(1)", "O(1)", "O(1)", "O(1)", "O(1)", "O(1)"]
}

complexity_df = pd.DataFrame(complexity_data)
complexity_df.to_excel("Time_Complexities.xlsx", index=False)

