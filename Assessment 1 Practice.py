animals_list = ['cat', 'horse', 'elephant', 'dog']
print(len(animals_list))

for animal in animals_list:
    print(len(animals_list))

    print(max(len(animals_list)))

longest()


# SIMPLE CALCULATOR
print("Please select operation -\n "

  	"1. Add\n"

  	"2. Subtract\n"

  	"3. Multiply\n"

  	"4. Divide\n")


# Take input from the user

select = int(input("Select operations form 1, 2, 3, 4 :"))

if select > 4:
    print('Error : Operation is not possible')

else:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

### YOUR CODE GOES HERE ###
if select == 1:
    x = number_1 + number_2
    print(' The answer is : {} '.format(x))
# Function to add two numbers

# Function to subtract two numbers
if select == 2:
    x = number_1 - number_2
    print(' The answer is : {} '.format(x))
# Function to multiply two numbers
if select == 3:
    x = number_1 * number_2
    print(' The answer is : {} '.format(x))
# Function to divide two numbers
if select == 4:
    x = number_1 / number_2
    print(' The answer is : {} '.format(x))


# Calculator logic



