def linear_search(arr,target):
    size = len(arr)
    for index in range(0,size):
        if (arr[index] == target):
            return index
    return -1    
my_list=[1,25,36,45,78,90]
target = 78
print(linear_search(my_list,target))