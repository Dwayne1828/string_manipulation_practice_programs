
full_name = input("Enter your full name with several spaces at the beginning: ")  # Input: "   John Doe"

# Remove the excess spaces at the beginning of the input
full_name = full_name.strip()

print(full_name)  # Output: "Your full name is: John Doe"