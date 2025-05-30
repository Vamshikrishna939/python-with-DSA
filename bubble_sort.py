
def bubble_sort(lst):
    n = len(lst)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we skip them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst 
lst=[12,9,4,15,23]
print(bubble_sort(lst))