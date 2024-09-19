# 3-1 -----------------

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))

print(f"Hello, {name}! You are {age} years old.")

# 3-2 -----------------

first = input("Please enter the first number: ")
second = input("Please enter the second number: ")

print(f"The sum of {first} and {second} is {float(first) + float(second)}")
print(f"The difference of {first} and {second} is {float(first) - float(second)}")
print(f"The product of {first} and {second} is {float(first) * float(second)}")
print(f"The quotient of {first} and {second} is {float(first) / float(second)}")

# 3-3 -----------------

temperature = float(input("Please enter the temperature in Celsius: "))

result = (temperature * 9 / 5) + 32

print(result)

# 3-4 -----------------

math_grade = float(input("Please enter your math grade: "))
english_grade = float(input("Please enter your english grade: "))
science_grade = float(input("Please enter your science grade: "))

total = math_grade + english_grade + science_grade
average = (math_grade + english_grade + science_grade) / 3

print(f"Total: {total}, Average: {average}")

# 3-5 -----------------

target = str(input("Please enter the target string: "))

print(f"Length: {len(target)}")
print(f"First character: {target[0]}")
print(f"Last character: {target[-1]}")

new_target = target * 3 # Repeat the string 3 times
print(f"New target: {new_target}")

# 3-6 -----------------

fruits = ["りんご", "バナナ", "オレンジ", "ぶどう", "メロン"]

print(f"a. {fruits[0]}")
print(f"b. {fruits[-1]}")
print(f"c. {fruits[2]}")
