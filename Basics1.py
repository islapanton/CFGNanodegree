# Intro
print('Hello World')
print('I hope it is sunny this weekend')

# Strings
print('cat' * 3) # will repeat string
print('cat'.upper()) # puts into capitals
print('Cat'.lower()) # puts into lowercase
print('Harry potter and the philosophers stone'.title()) # puts into titlecase
# Output of print is not remembered anywhere.
# If you are wanting to store information, might be useful to put into a variable

# Variables
# A variable can be put anywhere that a data value can be used

username = 'Isla1998'
age = 23
print('The person with the username', username, 'is', age, 'years old.')
# Whenever you change the value of the variable, it will be overwritten

# String Formatting
# Define the variables
oranges = 12
cost_per_orange = 0.5
# Calculate the total cost of 12 oranges
total_cost = oranges * cost_per_orange
# Create a new variable called output that we will use for the print statement
output = '{} oranges costs £{}'.format(oranges, total_cost)
print(output)

# Cat Food Exercise
cats =  3
cans_per_day = 2
total_cans = cats * cans_per_day
output = '{} cats will need {} cans of cat food'.format(cats, total_cans)
print(output)

# Join Strings
guests = 'Mary', 'Pete', 'Eoin'
print('We are going to the cinema with my classmates: {names} and me.'\
    .format(names=' , '.join(guests)))

# String Slicing
# Removing last 3 characters
S = 'ABCDEFGHI'
print(S[0:6])

# Slice from beginning to end with step 2
S = 'ABCDEFGHI'
print(S[0:9:2])

# Get CD using 2 different slicing ways:
print(S[2:4])
print(S[-7:-5])

# Inbuilt Functions
type('Code') # Returns the type of variable
len('Code') # Counts number of characters
ord('C') # Returns the unicode code of a given character. Unicode is a standard for consistent encoding, representation and handling of text.
\
