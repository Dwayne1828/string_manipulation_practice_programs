
#Asks the user for incorrect casing full name
incorrect_case_name = input("Please enter full name in incorrect casing: ")

#Corrects the casing of the full name
correct_case_name = incorrect_case_name.title()
pascal_case_name = "".join(correct_case_name)

print(pascal_case_name)