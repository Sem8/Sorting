# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for u in range(len(arr)):
        smallest_index = u
        for s in range(u + 1, len(arr)):
            if arr[s] < arr[smallest_index]:
                smallest_index = s
        arr[u], arr[smallest_index] = arr[smallest_index], arr[u]

    return arr

# My selection sort attempt that also works!!!
# def selection_sort( arr ):
#     for u in range(len(arr)):
#         # smallest_index = u
#         for s in range(u + 1, len(arr)):
#             if arr[s] < arr[u]:
#                 # smallest_index = s
#                 arr[u], arr[s] = arr[s], arr[u]

#     return arr

# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1): 
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr