


# creating the function to search in linear method


def located_card(cards, query):
    position = 0
    # Set up the while loop for the repetition
    while True:
        # check if the element is present in the current position or not
        if cards[position] == query:
            # Answer found and return and exit
            return position
        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found 
            return -1



# collection_list = [0,11,55,78,98,101,234,45]
# print(located_card(collection_list, 234))


def linear_search(array, target):
    # You can check wheather what you are receiving  in the arguments
    print(array)
    print(target)

    #checking if the list is empty if it is empty we will return -1
    if len(array) == 0:
        return -1
    position = 0

    #Setting the while loop for itrating the each loop
    while True:
        # checking if the element is present in the current list or not
        if array[position] == target:
            return position
        # increase the position by increament
        position += 1

        # checking if we have reached at the end of the list and the array is not present
        if position == len(array):
            return -1
        


# collection_list = [0,11,55,78,98,101,234,45]
# print(linear_search(collection_list, 100))


# Here while using the many if statement we can also follow this statement

def linear_method(array, target):
    position = 0
    #Directly check if the array of list is empty if yes then print -1 and the function if not then proceed to the next statement
    while position < len(array):
        if array[position] == target:
            return position
        position += 1
    return -1


collection_list = [0,11,55,78,98,101,234,45]
print(linear_method(collection_list, 99))


