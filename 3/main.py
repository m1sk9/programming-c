# ---------------------------------------------------------

def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))  # 8

# ---------------------------------------------------------

def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(4))
print(is_even_or_odd(7))

# ---------------------------------------------------------

def concat_lists(list1, list2):
    return list1 + list2

print(concat_lists([1, 2], [3, 4]))  # [1, 2, 3, 4]

# ---------------------------------------------------------

def profile(name, age="Unknown"):
    return f"Name: {name}, Age: {age}"

print(profile(name="Alice", age=25))
print(profile(name="Bob"))

# ---------------------------------------------------------

import math

num = float(input("Please enter a number: "))

sqrt_value = math.sqrt(num)

print(f"The square root of {num} is {sqrt_value}.")

# ---------------------------------------------------------

import math as m

degree = float(input("Please enter the degree: "))

radian = m.radians(degree)
sin_value = m.sin(radian)

print(f"The sine value of {degree} degrees is {sin_value}.")

# ---------------------------------------------------------

from math import pow

base = float(input("Please enter the base: "))
exponent = float(input("Please enter the exponent: "))

result = math.pow(base, exponent)

print(f"{base} raised to the power of {exponent} is {result}.")

# ---------------------------------------------------------

import math

num = float(input("Please enter a number: "))
print(f"The floor value of {num} is {math.sqrt(num)}.")

angle = float(input("Please enter the angle in degrees: "))
print(f"sin({angle}) = {math.sin(math.radians(angle))}")
print(f"cos({angle}) = {math.cos(math.radians(angle))}")

num = int(input("Please enter a number: "))
print(f"The factorial of {num} is {math.factorial(num)}.")

# ---------------------------------------------------------

import random

dice_rolls = []
for i in range(10):
    dice_rolls.append(random.randint(1, 6))
print(dice_rolls)
