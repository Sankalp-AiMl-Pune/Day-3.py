# Day 8 - Functions in Python
# GitHub 30 Days Challenge

def greet(name):
    print(f"Hello, {name}! Welcome to Day 8")

def add(a, b):
    return a + b

# Main code
greet("Rudra")

num1 = 10
num2 = 20
result = add(num1, num2)
print(f"{num1} + {num2} = {result}")

# Function with loop
def table(n):
    print(f"\nTable of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table(5)

print("\nDay 8 Completed!")
