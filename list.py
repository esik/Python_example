# Timer 1-20
for value in range(1,20):
    print(value)

# List 1 to million(min,max,sum)
numbers = list(range(1,1000001))
print("SUM",sum(numbers))
print("MIN",min(numbers))
print("MAX",max(numbers))

# odd number
for numbers in range(1,21,3):
    print(numbers)

# multiplicity 3
for numbers in range(3,31,3):
    print(numbers)

# cube
squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares)

# generate cube
squares = [value**3 for value in range(1,11)]
print(squares)

