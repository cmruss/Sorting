number1 = [9,7,6,8,5,2,1,3,4,112,0]
number2 = [9,7,6,8,5,2,1,3,4,112,0]
# # ITERATIVE
# def factorial(n):
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#     return total

# Rules of recursion
# 1. Must have a base case.
# 2. Must change state toward the base case.
# 3. Must call itself, recursively.

# RECURSIVE
def factorial(n):
    # set the base case
    while n <= 1:
        # if less than 1 return 1 
        return 1
    # return factorial of the next value multiplied by the current value
    return n * factorial(n - 1)

# print(factorial(5))

def quick_sort( arr ):
    # Base case arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    smaller = quick_sort(smaller)
    larger = quick_sort(larger)
    return smaller + [pivot] + larger

# print(quick_sort(numbers))



# TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO
#     step = 0
#     for i, (a, b) in enumerate(zip(arrA, arrB)):
#         cur_index = step + i
#         step = step + 1

#         print(f"cur_index: {cur_index}, merged_arr: {merged_arr} ")
#         print(f"a: {a}, b: {b}")
#         print(f"merged len {len(merged_arr)}")
#         if a < b:
#             merged_arr[cur_index], a = a, merged_arr[cur_index]
#             merged_arr[cur_index + 1], b = b, merged_arr[cur_index + 1]
#         else:
#             merged_arr[cur_index], b = b, merged_arr[cur_index]
#             merged_arr[cur_index + 1], a = a, merged_arr[cur_index + 1]
#         print(merged_arr)
    
#     return merged_arr

def merge( arrA, arrB ):
    els = len(arrA) + len(arrB)
    merged_arr = [0] * els
    a, b = 0, 0
    for i in range(els):
        if len(arrA) <= a:
            merged_arr[i] = arrB[b]
            b += 1
        elif len(arrB) <= b: 
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] > arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1
        else:
            merged_arr[i] = arrA[a]
            a += 1
    return merged_arr

# print(merge(number1,number2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len( arr ) <= 1:
        return arr
    mid = len(arr)//2
    first = arr[:mid]
    second = arr[mid:]
    # print(f"f: {first}, s: {second}")
    first = merge_sort(first)
    second = merge_sort(second)
    # print(f"f: {first}, s: {second}")
    merged_arr = merge(first, second)
    print(f"m: {merged_arr}")

    return merged_arr

print(merge_sort(number1))


def bradys_merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # initialize pointers
    a = 0
    b = 0
    for i in range(elements):
        # if index of a is greater than or equals length of arrA..
        if a >= len(arrA):
            # add b to the next index in merged_arr
            merged_arr[i] = arrB[b]
            #increment index of b
            b += 1
        # if index of b is greater than or equals length of arrB..
        elif b >= len(arrB):
            # add a to the next index in merged_arr
            merged_arr[i] = arrA[a]
            # increment index of a
            a += 1
        # if value of a is greater than value of b
        elif arrA[a] < arrB[b]:
            # assign value for current index of merged_arr current value of index a
            merged_arr[i] = arrA[a]
            # increment index a
            a += 1
        else:
            # else assign value for current index merged_arr, current value of index b
            merged_arr[i] = arrB[b]
            # increment index b
            b += 1
    return merged_arr

def bradys_merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = bradys_merge_sort(left)
    right = bradys_merge_sort(right)

    return bradys_merge(left,right)

# print(bradys_merge_sort(number1))



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
