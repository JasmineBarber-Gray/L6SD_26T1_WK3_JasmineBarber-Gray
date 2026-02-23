# Rugby Players Sorting and Timing Script
# Author: NZRU Data Analysis Example
# Description: 
# Sort rugby player ages using multiple algorithms, test on different datasets,
# record timings, print sample sorted data, and save results + complexities to Excel.

import pandas as pd
import random
import time

# Load the dataset
df = pd.read_excel(r"C:\Users\DELL 5520\Downloads\rugby_players_data-1.xlsx")

# Inspect dataset
print("Dataset preview:")
print(df.head())
print("\nColumns in dataset:", df.columns)

# Extract Age column and remove missing values
ages = df["Age"].dropna().tolist()
print(f"\nNumber of players with age data: {len(ages)}\n")

#Define sorting algorithms
# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # Stop early if already sorted
            break
    return arr

# 2. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 3. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
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

# 5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 6. Heap Sort
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

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Prepare test datasets
unsorted_data = ages.copy()                   # Original unsorted data
sorted_data = sorted(ages)                    # Sorted ascending
reverse_data = sorted(ages, reverse=True)    # Sorted descending
duplicate_data = ages + ages[:10]            # Duplicate some entries
empty_data = []                               # No data

# Shuffle datasets to create unorganized versions
random.shuffle(unsorted_data)
random.shuffle(duplicate_data)
# Empty_data remains empty

# Store all test cases in a dictionary
test_cases = {
    "Sorted": sorted_data,
    "Unsorted": unsorted_data,
    "Duplicate": duplicate_data,
    "Reverse": reverse_data,
    "No Data": empty_data
}

# Timing function
def time_sort(func, data):
    start = time.perf_counter()
    func(data.copy())
    end = time.perf_counter()
    return end - start

# Run sorting tests and print sample data
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

results = {}

for alg_name, alg_func in algorithms.items():
    print(f"\n--- Testing {alg_name} ---")
    results[alg_name] = {}  # Initialize nested dictionary
    for case_name, data in test_cases.items():
        
        # Time the sorting
        time_taken = time_sort(alg_func, data)
        results[alg_name][case_name] = time_taken

        # Get sorted output for verification
        sorted_sample = alg_func(data.copy())
        print(f"{case_name} (first 10): {sorted_sample[:10]} | Time: {time_taken:.6f} sec")

#Define theoretical complexities
complexity_data = {
    "Algorithm": ["Bubble","Insertion","Selection","Merge","Quick","Heap"],
    "Sorted": ["O(n²)","O(n)","O(n²)","O(n log n)","O(n log n)","O(n log n)"],
    "Unsorted": ["O(n²)","O(n²)","O(n²)","O(n log n)","O(n log n)","O(n log n)"],
    "Duplicate": ["O(n²)","O(n²)","O(n²)","O(n log n)","O(n log n)","O(n log n)"],
    "Reverse": ["O(n²)","O(n²)","O(n²)","O(n log n)","O(n log n)","O(n log n)"],
    "No Data": ["O(1)"]*6
}

#Save results and complexities to Excel
timing_df = pd.DataFrame(results).T.reset_index().rename(columns={"index":"Algorithm"})
complexity_df = pd.DataFrame(complexity_data)

with pd.ExcelWriter("Rugby_Sort_Results.xlsx") as writer:
    timing_df.to_excel(writer, sheet_name="Timing Results", index=False)
    complexity_df.to_excel(writer, sheet_name="Complexity Table", index=False)


print("\nAll results saved to Rugby_Sort_Results.xlsx")
