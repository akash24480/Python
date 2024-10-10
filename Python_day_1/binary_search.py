




# This is the first try made by me
# def binary_search(array, target):
#     if len(array) == 0:
#         return -1
#     mid = len(array) / 2
#     left = 0
#     right = 0

#     if mid[array] == target:
#         return mid[array]
#     if mid[array] > target:
        



# This is for the descending order 


def binary_search(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array)- 1


    while left <= right :
        mid = (left  + right) // 2
        mid_value = array[mid]

        print("left :", left, " right :", right, " mid :", mid, " mid_Value :", mid_value)

        if mid_value == target:
            return mid
        elif mid_value < target:
            right = mid - 1
        elif mid_value > target:
            left = mid + 1
 
    return -1


# collection_list = [0,11,55,78,98,101,234]
# print(binary_search(collection_list, 234))  # Here the number not found so it returns -1


# This is for the ascending order 


def binary_search(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array)- 1


    while left <= right :
        mid = (left  + right) // 2
        mid_value = array[mid]

        print("left :", left, " right :", right, " mid :", mid, " mid_Value :", mid_value)

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        elif mid_value > target:
            right = mid - 1
 
    return -1


# collection_list = [0,11,55,78,98,101,234]
# print(binary_search(collection_list, 7))  # Here the number not found so it returns -1



# What if the array contains the repeating element then how we can find that 

# arr = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0] in this case we will use the helper function to check that how to solve it

# Here the helper function

def helper_function(array, mid, target):
    mid_value = array[mid]
    print("mid:", mid, " mid_value:", mid_value)
    if mid_value == target:
        if mid -1 >= 0 and array[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif mid_value < target:
        return 'left'
    else:
        return 'right'


def repeated_number(array, target):
    left = 0
    right = len(array)- 1


    while left <= right :
        print("left :", left, " right :", right)
        mid = (left  + right) // 2
        result = helper_function(array, mid, target)


        if result == 'found':
            return mid
        elif result == 'left':
            right = mid - 1
        elif result == 'right':
            left = mid + 1
            
    return -1


collection_list = [0,0,0,2,2,2,3,6,6,6,6,6,6,8,8]

print(repeated_number(collection_list, 6))  # Here the number not found so it returns -1



