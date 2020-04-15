numbers = [9,7,6,8,5,2,1,3,4,112,0]
# TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
#         for j in range(0, len(arr)):
#             # print(f"index: {i} sub-index: {j}")
#             if arr[j] > arr[cur_index]:
#                 # print(f"{arr[j]} > {arr[cur_index]}")
#                 # index assignment swap
#                 arr[i], arr[j] = arr[j], arr[i]
#                 # print(arr)
#                 # smallest_index = j
#                 # print(f"smallest_index is now: {arr[smallest_index]}")
#         # TO-DO: swap   
#         # print(arr[i], arr[j])
#         # another.. index assignment swap.?
#         arr[i], arr[j] = arr[j], arr[i]
#         # print(arr[i], arr[j])
#         # print(arr)
#     return arr

# print(selection_sort(numbers))

# MY SOLUTION
def selection_sort( arr ):
    for i in range(0, len(arr)):
        cur_index = i
        for j in range(0, len(arr)):
            if arr[j] > arr[cur_index]:
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    return arr

# print(selection_sort(numbers))

# BRADY'S SOLUTION
def bradys_selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        print(arr)

    return arr

# print(bradys_selection_sort(numbers))

def brady_insertion_sort(arr):
    # loop through the array, setting the first index
    for i in range(1, len(arr)):
        # make a new array with the current value
        temp = arr[i]
        # connect/initialize the next loop..?
        j = i
        # nested loop index until new array and original array are the same length
        # and the index is greater than zero..?
        while j > 0 and temp <= arr[j - 1]:
            # move the index vlaues of existing values for displacement 
            # index assignment swap
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        print(arr)

    return arr

# print(f"insertion sort{insertion_sort(numbers)}")

# MY SOLUTION
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # for loop adjusted for array 
    for i in range(len(arr) -1, 0, -1):
        # nested for loop
       for j in range(i):
           # compares neighbors and then acts accordingly
           if arr[j] > arr[j + 1]:
                # index assignment swap
               temp = arr[j]
               arr[j] = arr[j + 1]
               arr[j + 1] = temp
    return arr

# print(f"bubble_sort{bubble_sort(numbers)}")

# BRADY'S SOLUTION
def bradys_bubble_sort( arr ):
    swaps_occured = True
    while swaps_occured:
        swaps_occured = False
        for i in range(len(arr) -1):
            print(arr)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occured = True
    return arr
            



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
