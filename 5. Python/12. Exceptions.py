import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid Input!")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot be divided by Zero!")
    sys.exit(1)

print(f"Value of {x} / {y} is : {result}")