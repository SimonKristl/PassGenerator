import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']
print ("Generátor náhodného hesla")

number_letter = int (input ("Zadejte počet písmen které má heslo obsahovat\n"))
number_number = int (input ("Zadejte kolik čísel má heslo obsahovat\n"))
number_special = int (input ("zadejte počet speciálnách znaků kolik má heslo obsahovat\n"))
result = []

for index in range (0, number_letter):
    random_number = random.randint (0, len(letters)-1)
    result. append(letters [random_number])
for index in range (0, number_number):
    random_number = random.randint (0, len(numbers)-1)
    result. append(numbers [random_number])
for index in range (0, number_special):
    random_number = random.randint (0, len(special_char)-1)
    result. append(special_char [random_number])
# print(result)
random.shuffle(result)
result_password = ""
for one_character in result:
    result_password += one_character
print(result_password)
