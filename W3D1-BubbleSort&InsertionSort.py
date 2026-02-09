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