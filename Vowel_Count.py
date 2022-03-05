string = input("Enter a string \n")
string = string.upper()
vowels = 0
for i in string:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        vowels += 1
print("Number of vowels are:")
print(vowels)