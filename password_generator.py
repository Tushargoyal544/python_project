import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

user_letter=int(input("enter the number of letter\n"))

user_number=int(input("enter the number of number\n"))

user_symbols=int(input("enter the number of symbols"))

password=[""]

for char in range(1,user_letter+1):
    password.append(random.choice(letter))

for char in range(1,user_number+1):
    password.append(random.choice(numbers))

for char in range(1,user_symbols+1):
    password.append(random.choice(symbols))

# print(password)

random.shuffle(password)
final_pass=""
for char in password:
    final_pass+=char
print(final_pass)