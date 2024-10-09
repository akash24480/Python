




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


collection_list = [0,11,55,78,98,101,234]
print(binary_search(collection_list, 234))  # Here the number not found so it returns -1


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


collection_list = [0,11,55,78,98,101,234]
print(binary_search(collection_list, 234))  # Here the number not found so it returns -1







