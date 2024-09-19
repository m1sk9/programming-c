first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))

result = first + second
print(result)

# ---------------------------------------------------------

def calculate_and_check(first, second):
    result = first + second
    if result > 10:
        print("Result is greater than 10")
    else:
        print("Result is less than 10")

calculate_and_check(7, 5)

# ---------------------------------------------------------

age = 19
name = "Sho"
is_student = True

print(age)
print(name)
print(is_student)

# ---------------------------------------------------------

first = 10
second = 3.14
third = "Hello"

print(type(first))
print(type(second))
print(type(third))

# ---------------------------------------------------------

name = "Sho"
age = 19

print(f"My name is {name} and I am {age} years old.")

# ---------------------------------------------------------

first = 15
second = 4

print(f"The sum of {first} and {second} is {first + second}")
print(f"The difference of {first} and {second} is {first - second}")
print(f"The product of {first} and {second} is {first * second}")
print(f"The quotient of {first} and {second} is {first / second}")
print(f"The remainder of {first} and {second} is {first % second}")

# ---------------------------------------------------------

first = 8
second = 12

is_greater = first > second
is_equal = first == second
is_lesser = first < second

print(is_greater)
print(is_equal)
print(is_lesser)

# ---------------------------------------------------------

first = True
second = False

and_result = first and second
or_result = first or second
not_result = not first

print(and_result)
print(or_result)
print(not_result)

# ---------------------------------------------------------

name = str(input("Please enter your name: ")) # `input()` のみと同等
age = int(input("Please enter your age: "))

print(f"Hello, {name}! You are {age} years old.")

# ---------------------------------------------------------

first = input("Please enter the first number: ")
second = input("Please enter the second number: ")

result = float(first) + float(second)
print(result)

# ---------------------------------------------------------

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))

print(f"Name: {name}, Age: {age}")
