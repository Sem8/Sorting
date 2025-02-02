# TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     merged_arr = arrA + arrB   
#     return merged_arr

# def merge( arrA, arrB ):
#   for i in arrB:
#     arrA.append(i)
#   return arrA

# def merge( arrA, arrB ):
#   merged_arr = [*arrA, *arrB]
#   return merged_arr
  
# def merge( arrA, arrB ):
#   arrA.extend(arrB)
#   return arrA

def merge( arrA, arrB ):
    merged_arr = []
    while arrA and arrB:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))            
        else:
            merged_arr.append(arrA.pop(0))          
    while arrA:
        merged_arr.append(arrA.pop(0))

    while arrB:
        merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
  if len(arr) == 1:
    return arr
  elif len(arr) == 0:
      return []

  # else:
  arrayOne = arr[:len(arr) // 2]
  arrayTwo = arr[len(arr) // 2:]

  arrayOne = merge_sort(arrayOne)
  arrayTwo = merge_sort(arrayTwo)
  arr = merge(arrayOne, arrayTwo)
  # print(arr)
  return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]

print(merge_sort(arr1))
print(merge_sort(arr2))
print(merge_sort(arr3))
print(merge_sort(arr4))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
