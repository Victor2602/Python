import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]
p=""
for nrl in range(1,nr_letters+1):
    let=random.choice(letters)
    password+=let
for nrl in range(1,nr_symbols+1):
    sym=random.choice(symbols)
    password+=sym
for nrl in range(1,nr_numbers+1):
    num=random.choice(numbers)
    password+=num
for nrl in range(1,len(password)+1):
    ranpass=random.choice(password)
    p+=ranpass
    #The random.shuffle() function do the same.
print(f"Your password is: {p}")
