#HomeWork 3
#Task 1
# Question 1
todays_weather = input(' Is it raining outside today? y/n')
if todays_weather == 'y':
    print('Take an umbrella then! ')
elif todays_weather == 'n':
    print('You wont need an umbrella today')

# Question 2
# This is my altered code below:
my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if int(my_money) >= boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')

# I have put an int condition on the input and also changed the operator to greater than
# or equal to as previously it was wrong.

# Question 3
year_of_publication = int(input(' What year was the book written? '))

if year_of_publication >= 1800 and year_of_publication < 1811:
    print('Nineteenth Century, Noughties')
elif year_of_publication >= 1811 and year_of_publication <1821:
    print('Nineteenth Century, Tens')
elif year_of_publication >= 1821 and year_of_publication <1831:
    print('Nineteenth Century, Twenties')
elif year_of_publication >= 1831 and year_of_publication <1841:
    print('Nineteenth Century, Thirties')
elif year_of_publication >= 1841 and year_of_publication <1851:
    print('Nineteenth Century, Fourties')
elif year_of_publication >= 1851 and year_of_publication < 1861:
    print('Nineteenth Century, Fifties')
elif year_of_publication >= 1861 and year_of_publication <1871:
    print('Nineteenth Century, Sixties')
elif year_of_publication >= 1871 and year_of_publication <1881:
    print('Nineteenth Century, Seventies')
elif year_of_publication >= 1881 and year_of_publication <1891:
    print('Nineteenth Century, Eighties')
elif year_of_publication >= 1891 and year_of_publication <1901:
    print('Nineteenth Century, Nineties')
elif year_of_publication >= 1901 and year_of_publication <1911:
    print('Twentieth Century, Noughties')
elif year_of_publication >= 1911 and year_of_publication <1921:
    print('Twentieth Century, Tens')
elif year_of_publication >= 1921 and year_of_publication <1931:
    print('Twentieth Century, Twenties')
elif year_of_publication >= 1931 and year_of_publication <1941:
    print('Twentieth Century, Thirties')
elif year_of_publication >= 1941 and year_of_publication <=1950:
    print('Twentieth Century, Fourties')
## I am aware this is probably not the most efficient way to write this /
# solve this problem but it is all I could think of so far !! ##

# Task 2
# Question 1
# The mistake is that as the programme will start counting from 0, inputting 1 to print the first item on the shopping list will actually print the second item. By changing the number to 0 as below,
# the first item (“Oranges”) will print out and tell us what the first item is to buy.
shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board"
]
print(shopping_list[0])

# Question 2

chocolates = {
     'white': 1.50,

    'milk': 1.20,

    'dark': 1.80,

    'vegan': 2.00,
}
purchase = input('What chocolate are you wishing to purchase?  ')

if purchase == 'white':
    print('The cost is £1.50 for this chocolate')
if purchase == 'milk':
    print('The cost is £1.20 for this chocolate')
if purchase == 'dark':
    print('The cost is £1.50 for this chocolate')
if purchase == 'vegan':
    print('The cost is £2.00 for this chocolate')


# Question 3
import random
lotterynumbers = []

for x in range (0, 6):
    number = random.randint(1, 25)
    while number in lotterynumbers:
        number = random.randint(1, 25)
    lotterynumbers.append(number)

lotterynumbers.sort()

our_numbers= []
for i in range (0, 6):
    our_numbers = int(input(' Please select a lucky number between 1 and 25:   ')
print('Your selected numbers are {}. Good luck!' .format(our_numbers))

print('The selected lottery numbers are:  {}'. format(lotterynumbers))

count = 0

for number in our_numbers:
    if number in lotterynumbers:
        counter += 1
print('You have' + str(count) 'matching numbers! Congratulations!')

if count == 3:
    print('Congratulations, you win £20!')
if count == 4:
    print('Congratulations, you win £40!')
if count == 5:
    print('Congratulations, you win £100!')
if count == 6:
    print('Congratulations, you win £10000!')
if count == 7:
    print('Congratulations, you win £100000!')
# This code isn’t exactly running as expected but I think it may be an issue with my PyCharm at the moment?
# Everything seems to be producing errors but this is what I have so far!

# Task 3
# Question 1

# Pip is a package manager for python that allows you to install and call upon different packages, libraries and modules into your own code.
# It is an easy and user-friendly way of downloading and incorporating into our own Python environments.

# Question 2
# The issue here is that we are just opening the file on read only mode.
# To solve this, we must change the ‘r’ to another option such as

# Question 3
Song = open("Song", 'w+')
Song.write(
    "You could never know what it's like, Your blood like winter freezes just like ice," 
    "And there's a cold lonely light that shines from you"
    "You'll wind up like the wreck you hide behind that mask you use"
    "And did you think this fool could never win?"
    "Well look at me, I'm coming back again"
    "I got a taste of love in a simple way"
    "And if you need to know while I'm still standing, you just fade awa"
    "Don't you know I'm still standing better than I ever did"
    "Looking like a true survivor, feeling like a little kid"
    "I'm still standing after all this time"
    "Picking up the pieces of my life without you on my mind"
    "I'm still standing (Yeah, yeah, yeah)"
    "I'm still standing (Yeah, yeah, yeah)")
print(Song.read())
