# 3-1 -----------------------

numbers = []

for i in range(1, 6):
    num = int(input(f"{i}: Please enter the number: "))

    if num < 0:
        continue
    numbers.append(num)

print(f"Total: {sum(numbers)}, Average: {sum(numbers) / 5}")

# 3-2 -----------------------

for i in range(3):
    inputd_password = input("Please enter the password: ")

    if inputd_password == "password":
        print("Login successful")
        break
    else:
        print("Login failed")
        continue

# 3-3 -----------------------

numbers = []

for i in range(1, 6):
    num = int(input(f"{i}: Please enter the number: "))
    numbers.append(num)

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

print(f"Even: {count_even(numbers)}, Odd: {count_odd(numbers)}")

# 3-4 -----------------------

numbers = []

for i in range(1, 6):
    num = int(input(f"{i}: Please enter the number: "))
    numbers.append(num)

print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# 3-5 -----------------------

lower_limit = int(input("Please enter the lower limit: "))
upper_limit = int(input("Please enter the upper limit: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(lower_limit, upper_limit + 1) if is_prime(num)]

print(f"Primes between {lower_limit} and {upper_limit}: {primes}")

# 3-6 -----------------------

scores = []

for i in range(1, 6):
    score = int(input(f"{i}: Please enter the score: "))
    scores.append(score)

age_score = sum(scores) / 5

if age_score >= 80:
    result = "S"
elif age_score >= 60:
    result = "A"
else:
    result = "B"

print(f"Total: {sum(scores)}, Average: {age_score}, Grade: {result}")

# 3-7 -----------------------

fruits = ["apple", "banana", "orange", "grape", "melon"]

search_target = input("Please enter the target fruit: ")

if search_target in fruits:
    print(f"{search_target} is in the list.")
else:
    print(f"{search_target} is not in the list.")

# 3-8 -----------------------

n = int(input("Please enter an integer: "))

total = sum(range(1, n + 1))

print(f"The sum of numbers from 1 to {n} is: {total}")

# 3-9 -----------------------

words = []
count = 0

for i in range(1, 6):
    word = input(f"{i}: Please enter the word: ")
    words.append(word)

for i in words:
    if "a" in i:
        count += 1

print(f"Words with 'a': {count}")


