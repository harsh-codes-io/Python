word = input("Enter the word: ")

word = word.upper()
reversed_word = word[::-1]

if(word == reversed_word):
    print("Palindrome")

else:
    print("Not palindrome")