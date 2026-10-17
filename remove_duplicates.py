initial_list = input("Enter the list items seprated by space: ").split()

print(f"Initial Items in list: {initial_list}\n\n")

print(f"After removing the duplicates: {list(set(initial_list))}")