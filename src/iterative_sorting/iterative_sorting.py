# # TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    # return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        # temp = 0
        an_element = arr[i]        
        neighbor_element = arr[i+1]
        if an_element == neighbor_element or an_element < neighbor_element:
            pass
        elif an_element > neighbor_element:
            temp = an_element
            an_element = neighbor_element
            neighbor_element = temp            
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr