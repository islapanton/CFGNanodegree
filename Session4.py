# Indexes

#Exercise

scores = [3, 18, 45, 71, 76, 82, 104, 159, 188, 200]
print(len(scores)) # prints count of list
print(min(scores))
print(max(scores))
print()
print(sorted(scores, reverse= True)) # This will print list in reverse order

# In operator
student_name = input('Which student are you looking for?   ')
students = []

# Append
students = ['Dierdre']

# FINISH this Isla


# Using lists and for loops together
student_names = ['Dierdre', 'Hank', 'helena', 'Salome']
for student_name in student_names:
    print(student_name)

# Counting the number of items in list using a for loop
student_names = ['Dierdre', 'Hank', 'helena', 'Salome']
count = 0
for student_name in student_names:
    count = count + 1

print(count)

# Exercise
# I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
#Write a program that uses a for loop to calculate the total cost
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost

print('{:.2f}'.format(total_cost)) # formatting to give us 2 dp

# Using a for loop, output the values name, colour and price of each dictionary in the list
fruits = [
    {"name": "apple", "colour": "red", "price": 0.12},
    {"name": "banana", "colour": "yellow", "price": 0.2},
    {"name": "pear", "colour": "green", "price": 0.19},
]

for fruit in fruits:
    print("{} {} {}".format(fruit["name"], fruit["colour"], fruit["price"]))

### Exercise 4
# Write a list comprehension expression to build a new list that calculates the square for the number that are divisible by 2 in range(1, 6).

# Your sample output should be ```[4, 16]```
our_new_list = [x * x for x in range(1, 6) if x % 2 == 0]
print(our_new_list)
