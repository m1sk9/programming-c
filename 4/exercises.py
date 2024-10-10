# 3-1 ---------------

import numpy as np

start = int(input("Enter the start value of the range: "))
end = int(input("Enter the end value of the range: "))

array = np.arange(start, end + 1)
even_numbers = array[array % 2 == 0]

print(f"Even elements: {even_numbers}")

# 3-2 ---------------

import pandas as pd

data = {
    'Name': ['Anna', 'Ben', 'Cathy', 'Dave'],
    'Age': [23, 35, 45, 28]
}
df = pd.DataFrame(data)

print("People aged 30 and above:")
print(df[df['Age'] >= 30])

# 3-3 ---------------

import numpy as np

original_matrix = np.array([[2, 8, 4], [2, 9, 1], [4, 8, 0]])
new_matrix = original_matrix + 5

print("Original matrix:")
print(original_matrix)
print("Matrix after adding 5:")
print(new_matrix)

# 3-4 ---------------

import pandas as pd

data = {
    'Name': ['Emily', 'Frank', 'Grace', 'Hannah'],
    'Age': [29, 34, 26, 38]
}
df = pd.DataFrame(data)

max_age_person = df.loc[df['Age'].idxmax()]['Name']

print("Person with the highest age:", max_age_person)

# 3-5 ---------------

import numpy as np

array = np.random.randint(1, 100, 10)

mean_value = np.mean(array)
max_value = np.max(array)
min_value = np.min(array)

print("Array:", array)
print("Mean value:", mean_value)
print("Max value:", max_value)
print("Min value:", min_value)

# 3-6 ---------------

import pandas as pd

data = {
    'Name': ['Yoshii', 'Ishido', 'Toda', 'Kashiki'],
    'Age': [24, 45, 35, 29],
    'Occupation': ['Engineer', 'Doctor', 'Engineer', 'Teacher']
}

df = pd.DataFrame(data)

mean_age_by_occupation = df.groupby('Occupation')['Age'].mean()
print(mean_age_by_occupation)
