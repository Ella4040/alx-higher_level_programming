#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("The number is:", number)
if number < 0:
    print(f"{number} is negative")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is zero")
