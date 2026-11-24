# Declare two empty lists
first_list = []
second_list = []

# Populate the first list with two values
first_list.append(input("Enter the first value: "))
first_list.append(input("Enter the second value: "))

# Populate the second list with three values
second_list.append(input("Enter the third value: "))
second_list.append(input("Enter the fourth value: "))
second_list.append(input("Enter the fifth value: "))

# Combine the two lists into a single list
combined_list = first_list + second_list

# Remove the second element
combined_list.pop(1)

# Request another value and insert it in the middle
new_value = input("Enter another value: ")
combined_list.insert(len(combined_list) // 2, new_value)

# Display a slice from the second to the fourth element
print(combined_list[1:4])