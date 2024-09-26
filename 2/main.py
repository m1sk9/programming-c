# ---------------------------------------------------------

age = int(input("Please enter your age: "))

if age <= 18:
    price = 500
elif age >= 65:
    price = 300
else:
    price = 1000

print(f"The ticket price is {price} yen.")

# ---------------------------------------------------------

temp = float(input("Please enter the temperature in Celsius: "))

if temp <= 36.0:
    health_status = "Hypothermia"
elif temp >= 37.5:
    health_status = "Fever"
else:
    health_status = "Normal"

print(f"The health status is {health_status}.")

# ---------------------------------------------------------

score = int(input("Please enter your score: "))

if score >= 90:
    grade = "S"
elif score >= 70:
    grade = "A"
elif score >= 50:
    grade = "B"
else:
    grade = "E"

print(f"Your grade is {grade}.")

# ---------------------------------------------------------

score = int(input("Please enter your score: "))

if score >= 80:
    attendance = int(input("Please enter your attendance rate: "))

    if attendance >= 20:
        result = "Pass"
    else:
        result = "Fail"
else:
    result = "Retake"

print(f"The result is {result}.")

# ---------------------------------------------------------

room_type = input("Please enter the room type (single/double): ")
nights = int(input("Please enter the number of nights: "))

if room_type == "single":
    if nights >= 3:
        rate = 3000
    else:
        rate = 4500
elif room_type == "double":
    if nights >= 3:
        rate = 8000
    else:
        rate = 7500
else:
    rate = 0
    print("Invalid room type.")

total = rate * nights

if total > 0:
    print(f"The total cost is {total} yen.")

# ---------------------------------------------------------

age = int(input("Please enter your age: "))
is_member = input("Are you a member? (yes/no): ")

if age <= 18 and is_member == "yes":
    print("Admission")
else:
    print("No admission")

# ---------------------------------------------------------

age = int(input("Please enter your age: "))
attendance = int(input("Please enter your attendance rate: "))

if age >= 18 and attendance >= 10:
    print("Admission")
else:
    print("No admission")

# ---------------------------------------------------------

age = int(input("Please enter your age: "))
is_member = input("Are you a member? (yes/no): ")
has_coupon = input("Do you have a coupon? (yes/no): ")

if age >= 18 and is_member == "yes":
    print("Admission")
elif age >= 18 and has_coupon == "yes":
    print("Admission")
else:
    print("No admission")

# ---------------------------------------------------------

count = int(input("Please enter the number of items: "))
total = 0

for _ in range(count):
    price = int(input("Please enter the price of the item: "))
    total += price

print(f"The total cost is {total} yen.")

# ---------------------------------------------------------

text = input("Please enter the target text: ")

for i in range(5):
    print(text)

# ---------------------------------------------------------

upper_limit = int(input("Please enter the upper limit: "))
sum_even = 0

for n in range(1, upper_limit):
    if n % 2 == 0:
        sum_even += n

print(f"The sum of even numbers is {sum_even}.")

# ---------------------------------------------------------

numbers = [10, 20, 30, 40, 50]
total = 0

for n in numbers:
    total += n

print(f"The total is {total}.")

# ---------------------------------------------------------

fruits = ["apple", "banana", "orange", "grape"]

for i in fruits:
    print(i)

# ---------------------------------------------------------

while True:
    num = int(input("Please enter a number: "))
    if num == 0:
        break
print(f"Inputed number: {num}")
