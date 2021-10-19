# Question 1
todays_weather = input(' Is it raining outside today? y/n')
if todays_weather == 'y':
    print('Take an umbrella then! ')
elif todays_weather == 'n':
    print('You wont need an umbrella today')

# Question 2
my_money = input('How much money do you have? ')
boat_cost = 20 + 5

if int(my_money) >= boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')

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


# Question 4
shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board"
]
print(shopping_list[0])

# Question 5

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


# Question 6
import random
def lottery_numbers():
    ln = random.sample(range(1,30),7)
    print((ln.sort())
user_ticket = [3, 7, 14, 16, 22, 28, 29]


