#!/usr/bin/python3
import random
number = random.randint(-100, 100)
if number < 0:
    print(f"{number:a} is negative")
elif number > 0:
    print(f"{number:a} is positive")
else:
    print(f"{number:a} is zero")
