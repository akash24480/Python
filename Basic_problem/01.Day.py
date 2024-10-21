# Problem 1


def even_odd(num):
    if num % 2 == 0:
        return "even"
    return "odd"



# print(even_odd(4))




#problem 2 checking the given number is prime or not

def prime_num(num):
    if num <= 1:
        return "Not prime"
    num_check = 2
    while num_check * num_check <= num:
        if num % num_check == 0:
            return "Not Prime"
        num_check += 1
    return "Prime"

# print(prime_num(11))


#To check if the given num is leap year or not

def leap_year(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return "Leap"
            return "Not"
        return "Leap"
    return "Not"
    
    
    
# print(leap_year(2123))



# Calculating the Armstrong number

def armstrong(num):
    length = len(str(num))
    add_num = 0
    original_num = num

    
    while num > 0:           
        single_digit = num % 10
        add_num += pow(single_digit, length)
        num = num // 10
        
    if original_num == add_num:
            return "Armstrong"
        
    return "Not Armstrong"
        
    
    

# Test the function
# print(armstrong(153))  # Should print "Armstrong"
# print(armstrong(123))  # Should print "Not Armstrong"



# Here without using the POW built in function we achive the armstrong number

def arms(nums):
    length = len(str(nums))
    add_digit = 0
    original_num = nums
    while nums > 0:
        single_digit = nums % 10
        power = 1
        for _ in range(length):
            power = power * single_digit
        add_digit += power
        num = num // 10
    if original_num == add_digit:
        return "armstrong"
    return "Not armstrong"


# print(armstrong(153))  # Should print "Armstrong"
# print(armstrong(123))  # Should print "Not Armstrong"



#fibnocci series

def fibo(num):
    first = 0
    second = 1
    fib = []
    for _ in  range(num):
        fib.append(first)
        next_number = first + second
        first = second
        second = next_number
    return fib
        
        
        
        
# print(fibo(15))




# # Creating the armstrong number

# def practice(num):
#     original_num = num
#     add_num = 0
#     length = len(str(num))
#     while num > 0:
#         rem = num % 10
#         add_num += pow(rem, length)
#         num = num // 10
        
#     if original_num == add_num:
#         return "Arms"
    
#     return "Not Arms"

# print(practice(153))


# To check that the given string is palindrome or not

# def palindrome(word):
#     characters = list(word)
#     store_char = []
#     duplicate_char = ""
#     for char in characters:
#         store_char.append(char)
#     for duplicate in len(store_char)-1:
#         duplicate_char += duplicate
#     if duplicate_char == word:
#         return "palindrome"
#     return "Not Palindrome"
        
    
    
# print(palindrome("Mango"))     This is the first method tried with but failed

       
       
        




def palindrome(word):
    normalize_word = word.lower()
    reversed_word = ""
    for i in range(len(normalize_word) - 1, -1, -1):
        reversed_word += normalize_word[i]
     
    if reversed_word == normalize_word:  # Indentation fixed here
        return "Palindrome"  # Fixed spelling
    return "Not Palindrome"

# print(palindrome("alaa"))    




# Creating the different * patterns

  
  
    