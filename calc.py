numbers = tuple(map(int,input("Enter 5 numbers separated by space: ").split()))

total = sum(numbers)
print(f"Sum: {total}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Average: {round(total/len(numbers),2)}")