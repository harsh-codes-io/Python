from pathlib import Path

#printing the curent working directory
current_dir = Path.cwd() 
print(f"Current Working directory: {current_dir}")

#Loop through and printing all the items directly in current directory
#iterdir() method allow iteration over the current directory items 
for items in current_dir.iterdir():
    print(f"Items in directory: {items}")
    print(f"name of items: {items.name}")
    print(f"It is a file or not: {items.is_file()}")
    print(f"Extension of file: {items.suffix}")
