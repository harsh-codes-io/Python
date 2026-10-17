initial_list = input("Enter the list items seprated by space: ").split()

print(f"Initial Items in list: {initial_list}\n\n")

unique_list = list(dict.fromkeys(initial_list))

print(f"After removing the duplicates: {unique_list}")