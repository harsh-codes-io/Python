num1 ,num2 = map(int,input("Enter two number separated by space: ").split())

def add(num1,num2):
    return num1+num2

print(f"Addition of entered numbers {num1},{num2} is: {add(num1,num2)}")