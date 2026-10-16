from collections import Counter

sentence = input("Enter the sentence: ")

words = sentence.split()
counts = {}
counts = Counter(words)

for word,value in counts.items():
    print(f"word: {word} | Frequency: {value}")
    
