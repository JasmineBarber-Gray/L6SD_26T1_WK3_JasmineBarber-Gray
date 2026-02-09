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
        min_index - i
        for i in range(i=1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]
            return arr
                
#set data list
set_data = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

#sort data list
sorted_data = selection_sort(set_data)
print("Sorted data:", sorted_data)