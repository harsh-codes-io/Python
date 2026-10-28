from pathlib import Path

#printing the curent working directory
current_dir = Path.cwd() 
print(f"Current Working directory: {current_dir}")


#Iterating over directory items, and adding item in list if it is a file and have required suffix
json_metadata_files = [items for items in current_dir.iterdir() if items.is_file() and items.suffix.lower() == ".json"]

for json_file in json_metadata_files:
    print(json_file)