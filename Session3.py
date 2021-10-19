# Revision of For Loops
for number in range(9):
    print('~'* number)

# If Statements
password = input('password:   ')
if password == 'Treacle47':
    print('Success!')
# Used to run a block of code depending on whether a condition is true or flase
# == sign checks for exactly the same string (case sensitive)

# Exercise
price = input(' How much is a burger?   ')
vege = input('Is there a vegetarian option? (y/n)  ')
within_budget = float(price) <= 10.00
has_vege = vege == 'y'
is_good_choice = within_budget and has_vege

if within_budget and has_vege:
    print('This restaurent is a great choice !')
else:
    print ('Probably not a good idea')

# Else statements are used with an if statement and run when the if condition is false
password = input('password:   ')
if password == 'Treacle47':
    print('Success!')
else:
    print( 'Incorrect password. Try again')

# Exercise
meal_price = float(input('How much did the meal cost?   '))
discount_choice = input(' Do you have a discount code? y/n ')
discount_applicable = discount_choice == 'y'

good_meal_price = float(meal_price) => 20.00

if good_meal_price == TRUE:
    meal_price * 0.9
    print(Discount applied !)

# Palindrome
def isPalindrome(s):
    return s == s[::-1]
s = "racecar"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")


    def isPalindrome(string):
        l = len(string)
        if l == 1:
            print('True')
        return string == string[::-1]
isPalindrome('hannah')