import random

lower_limit ,upper_limit =  map(int,input("Enter the lower and upper limit seprated by space: ").split()) 

number = random.randint(lower_limit,upper_limit)
count = 0
while(True):
    guessed_number = int(input("Guess the number: "))
    count += 1
    if(guessed_number > number):
        print(f"Your guessed number {guessed_number} is greater than correct number")
    elif(guessed_number < number):
        print(f"Your guessed number {guessed_number} is less than correct number")
    else:
        print(f"Congratulations!\nCorrect number is {number}\nYou guessed correct number in {count} Attempts.")
        user_input = input("Wants to play again: Y/N :").upper()
        if(user_input != 'Y'):
            break
        else:
            count = 0
            lower_limit ,upper_limit =  map(int,input("Enter the lower and upper limit seprated by space: ").split())
            number = random.randint(lower_limit,upper_limit)

