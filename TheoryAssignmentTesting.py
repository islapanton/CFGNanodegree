text = "cats"
x = text.center(30)
print(x)

string = 'My cat is called Treacle and she is 13 years old'
print(string.startswith('My'))

string2 = 'BELFAST'
print(string2.isupper())

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.clear()
#Using print to show empty list
print(friends)

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
print(friends.copy())


string = "?????.....??????,,,,sjkI am meeting my friend"
print(string.lstrip('?.,sjk'))

string3 = '..... klk apple, banana, pear, grapes ///????'
print(string3.strip(' .kl/?'))

string4 = 'Harry potter aNd tHE Chamber oF secrets'
print(string4.swapcase())

shopping_list = ['Eggs', 'Avocado', 'Chocolate', 'Tomatoes', 'Cat food', 'Eggs']
print(shopping_list.count('Eggs'))

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
numbers= ['1', '4', '13']
friends.extend(numbers)
print(friends)


friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
print(friends.index('Mhari'))

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.insert(3, 'Erin')
print(friends)

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.pop(1)
print(friends)


friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.remove('Anna')
print(friends)

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.reverse()
print(friends)

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.sort()
print(friends)

tuple_a = (4, 12, 16, 17, 98, 2, 4, 2, 4)
print(tuple_a.index(98))

friends = ['Rosa', 'Alice', 'Anna', 'Mhari']
friends.append('Erin')
print(friends)

fruits = [
    {"name": "apple", "colour": "red", "price": 0.15},
    {"name": "banana", "colour": "yellow", "price": 0.20},
    {"name": "pear", "colour": "green", "price": 0.40},
    {'name': 'grapes', 'colour': "purple", 'price': 1.00}
]
fruits.clear()
print(fruits)

fruits = [
    {"name": "apple", "colour": "red", "price": 0.15},
    {"name": "banana", "colour": "yellow", "price": 0.20},
    {"name": "pear", "colour": "green", "price": 0.40},
    {'name': 'grapes', 'colour': "purple", 'price': 1.00}
]
fruits.copy()
print(fruits)

apple = {"colour": "red", "price": 0.15}
print(apple.fromkeys('p'))

apple = {"colour": "red", "price": 0.15}
print(apple.get('colour'))

dict1 = {'a': 2, 'b': 5, 'c': 9}
print(dict1.fromkeys('def'))

apple = {"colour": "red", "price": 0.15}
print(apple.items())

apple = {"colour": "red", "price": 0.15}
print(apple.keys())

exam_results = {'English': 'A', 'Maths': 'A', 'Biology': 'A', 'German': 'B'}
new_result = {'Modern Studies': 'A'}
exam_results.update(new_result)
print(exam_results)

exam_results = {'English': 'A', 'Maths': 'A', 'Biology': 'A', 'German': 'B'}
print(exam_results.values())

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
chocolate.add('Salted Caramel')
print(chocolate)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
chocolate.clear()
print(chocolate)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
choc2 = chocolate.copy()
print(choc2)

set1 = {1, 44, 83, 19}
set2 = {7, 44, 36, 21}

set3 = set1.difference(set2)
print(set3)

set1 = {1, 44, 83, 19}
set2 = {7, 44, 36, 21}
set3 = set1.intersection(set2)
print(set3)

set1 = {1, 2, 3, 4}
set2 = {7, 6, 5, 4, 3, 2, 1}
set3 = set1.issubset(set2)
print(set3)

set1= {100, 90, 85, 70, 60, 50}
set2 = {50, 60, 70}
set3 = set1.issuperset(set2)
print(set3)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
chocolate.remove('Mint')
print(chocolate)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
chocolate.pop()
print(chocolate)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
choc2 = {'Dark', 'Salted Caramel', 'White', 'Aero'}
choc3 = chocolate.symmetric_difference(choc2)
print(choc3)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
chocolate2 = {'Dark', 'Salted Caramel', 'White', 'Aero'}
chocolate3 = chocolate.union(chocolate2)
print(chocolate3)

chocolate = {'Milk', 'Dark', 'White', 'Mint'}
chocolate2 = {'Dark', 'Salted Caramel', 'White', 'Aero'}
chocolate.update(chocolate2)
print(chocolate)
