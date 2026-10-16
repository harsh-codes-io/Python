number = int(input("Enter the number: "))
upper_limit = int(input("Enter the number to which table required: "))

for i in range(1,upper_limit+1):
    print(f"{number} X {i} = {number*i}")