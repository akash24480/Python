#Using the hashmap finding the sum in the array


def two_sum(nums, target):
    prevMap = {} # value : index    #mapping the value with the index
    for i, n in enumerate(nums):   # i is the index and n is the value
        diff = target - n  
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return
arr = [3,1]   # The target is to find the 4


# print(two_sum(arr, 4))


#The bruteforce model 

def practice(nums, target):
    prevmap = {}  #In the dictionary to use the key value pair
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevmap:
            return [prevmap[diff], i]
        prevmap[n] = i
    return





# print(two_sum(arr, 4))



#Finding the duplicate integer in the given array
def hasDuplicate(arr):
    duplicateNum = set()
    for i in arr:
        if i in duplicateNum:
            return True
        duplicateNum.add(i)
        print(duplicateNum)
    return False

arr = [1,2,3,4,1]
# print(hasDuplicate(arr))


def isAnagram(s, t):
    secondC = t
    store = set()
    for first in s:
        if first in secondC:
            print(first, secondC)
            
            return True
        print(first, secondC)
    return False


s= "jam"
t= "jar"
print(isAnagram(s,t))







            
    

