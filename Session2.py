# Input
friends = input('How many friends are round?  ')
pizzas = int(friends) * 0.5
print('You need {} pizzas for {} friends'.format(pizzas, friends))

# Python modules
# A module is a code that someone else has written (imported in python programmes)


word = input('Enter the word you would like to encode:  ')
result= ''
for char in word:
    encoded= 'xyz{}abc'.format(char)
    result=result + encoded

    print(result )


# Args and Kwargs Examples
def multiply(x, y):
    print (x * y)

multiply(5, 4)  #Runs as expected

multiply(5, 4, 3) # This will throw an error as only 2 arguments were defined in the function

# Instead if we define multiply with *args as the function parameters we have much more flexible code
def multiply2(*args):
    z= 1
    for num in args:
        z *= num
    print(z)
multiply2(4, 5) # Works as above
multiply2(3, 5, 10, 23) # But can also work with multiple arguments

# Kwargs Example
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)

### EXERCISE 2 ###
"""
Write a program that issues notifications to drivers about PCN (Penalty Charge Notice) for £130. 
If a person pays within 14 days, then the amount will be reduced to £65.

Pseudo-code Example:

- Accept the PCN date as an input
- Calculate the deadline date, which is 14 days from the PCT issue date.
- Print the message informing the driver about the deadline date, so that they only need to pay £65.
.
"""



### EXERCISE 3 ###
"""
fetch current date and time to milliseconds and create a "timestamp" in the following format YYYYMMDD_HHMMSSMsMs

For example: if the current date and time is "30 October 2020, 10h 25 min 41 sec and 123456 milliseconds", out timestamp must be:

"20201030_22254112"

"""
# import datetime
#
# dt = datetime.datetime.now()
# print(dt) # check what we get back
#
# timestamp = "your solution is here"
#
# print("timestamp: " + timestamp)






### EXERCISE 4 ####
"""
Write a very simple encoding program that accepts a word from a user and encodes it 
by wrapping each letter with some other letters (symbols).

Complete this together with the group
"""


### DEMO 5 ###
"""
Due to social disctancing, only 10 people are allowed to be inside a shot at the same time. 
This program invites people in the queue to come in while we have some capacity.
"""



### DEMO 6 ###
"""
Example INFINITE 'while loop' that runs forever until the memory is 'blown'
"""




### DEMO & EXERCISE 7 ###
"""
Create functions, call functions and pass arguments.
Talk class through all examples. 
"""



"""
Pass Arguments
 - You can send information to a function by passing values, known as arguments.
 - Arguments are declared after the function name in parentheses.
 - When you call a function with arguments, the values of those arguments are copied to their corresponding parameters inside the function.
"""




### DEMO & EXERCISE 8 ###

"""
Positional Arguments

Positional arguments values are copied to their corresponding parameters in order.
You must to pass arguments in the order in which they are defined.
"""



"""
Keyword Arguments

you can pass arguments using the names of their corresponding parameters.
in this case, the order of the arguments no longer matters.
you can combine positional and keyword arguments in a single call.
if you do so, specify the positional arguments before keyword arguments.
"""



"""
Default Arguments¶
You can specify default values for arguments when defining a function.
The default value is used IF the function is called without a corresponding argument.
"""



"""
Variable Length Arguments (*args and **kwargs)¶
Variable length arguments are useful when you want to create functions that take unlimited number of arguments.
Unlimited in the sense that you do not know beforehand how many arguments can be passed to your function by the user.

*args¶
When you prefix a parameter with an asterisk *, it collects all the unmatched positional arguments into a tuple
(we will learn about tuples later, think of it as a collection of items aka a box with numbers or words etc) .
'''
def print_arguments(*args):
    print(args)
print_arguments(1,2,3,4,5,6,7)


**kwargs
The ** syntax is similar, but it only works for keyword arguments (aka corresponding pairs)
"""



### DEMO & EXERCISE 9 ###
"""
Examples how to return values from a function.
"""



### EXERCISE 10 ###
"""
Complete the function to return the area of a circle
"""

# def circle_area():  # add the radius argument inside the brackets
#     area = 3.14 * (radius ** 2)
#     # return area here
#
#
# circle_1 =  circle_area(10)
#
# print(circle_1)\

# Instructor Version
