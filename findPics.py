from pathlib import Path

#printing the curent working directory
current_dir = Path.cwd() 
print(f"Current Working directory: {current_dir}")

pic_extensions = [".jpeg",".jpg",".heic",".png"]

#List comprehension 
#Iterating over directory items, and adding item in list if it is a file and have required suffix
pics = [items for items in current_dir.iterdir() if items.is_file() and items.suffix.lower() in pic_extensions]

for pic in pics:
    print(pic)
