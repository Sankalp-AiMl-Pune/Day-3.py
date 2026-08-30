# Day 5 - Even Odd Checker
num = int(input("Number dal: "))

if num % 2 == 0:
    print(f"{num} Even hai")
else:
    print(f"{num} Odd hai")

# Extra check
if num > 0:
    print("Positive number hai")
elif num < 0:
    print("Negative number hai")
else:
    print("Zero hai")
