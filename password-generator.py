#This is a password generator, I know that I could wrap the 3 for loop blocks into a single function to avoid code repetition, but at the time I was still learning python and didn't know about function yet! 
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#new list necessary to append the random choise (see line 25)
new_arr = []
#initialing the password as an empty string
password = ''

print("Welcome to the PyPassword Generator!")
#getting the 3 inputs
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
#Asking to the users if they wants to shuffle the characters
random_password_choice = str(input("Do you want to shuffle the characters ? Please type Yes or No to continue\n")).lower()

#looping to the input from the user (this code works the same for numbers and symbols)
for letter in range(0, nr_letters):
    #create a random letter
    random_letter = random.choice(letters)
    #add the random letter to the new_arr list
    new_arr.append(random_letter)

for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    new_arr.append(random_number)

for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    new_arr.append(random_symbol)
    
#conditional block necessary to check if the users wants their passwords shuffle it
if random_password_choice == 'no': 
    password = password.join(new_arr)
    print(f"Here's your new password: {password}")
elif random_password_choice == 'yes':
    random.shuffle(new_arr)
    password = password.join(new_arr)
    print(f"Here's your new password: {password}")
else:
    print("You've entered an invalid answer, please start the process over")