# Opening and reading a file
import csv

file = open('/Users/islapanton/Desktop/Data/example_one.txt', 'r')
content = file.read()
print(content)
file.close()

# Returns one line from the file
print(content.readline())


# Creating a new file and writing in it
file2 = open('our_new_file_for_writing.txt', 'w')
file2.write('Good evening guys and dolls')
print(file2.read())

# Context Managers
with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nRosa '
    text_file.write(people)
print(people.read())

# Exercise
import csv

with open('/Users/islapanton/Downloads/trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []


    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)

print(shortest_height)

# Problem Solving Tasks
# 1. Take the file name and the word to be counted from the user.
# 2. Read each line from the file and split the line to form a list of words.
# 3. Check if the word provided by the user and any of the words in the list are equal and if they are, then increment the word count.
fname = input("Enter file name: ")
word = input("Enter word to be searched:")
k = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if (i == word):
                k = k + 1
print("Occurrences of the word:")
print(k)
file.close()

  SOLUTION 1 -- it is OK
