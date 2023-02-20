# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_" + user_name + "!")
    
hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(num):
    return [x for x in range(0, + num + 1)if x % 2 != 0]
print(first_odds(100))

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max
print(max_num_in_list([10, 25, 90, 15]))

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0) and (year % 400 == 0):
            leap = True
        elif (year % 100 == 0) and (year % 400 !=0):
            leap = False
        else:
            leap = True
    return leap
input_year = int(input())
print(is_leap_year(input_year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True    
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 2, 4, 5]
  
print(is_consecutive(x))
print(is_consecutive(y)) 
