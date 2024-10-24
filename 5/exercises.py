# 3-1 ------------

students = [
    { 'name': 'Sato', 'total_score': 240 },
    { 'name': 'Suzuki', 'total_score': 240 },
    { 'name': 'Takahashi', 'total_score': 250 },
    { 'name': 'Tanaka', 'total_score': 249 },
    { 'name': 'Ito', 'total_score': 253 },
]

print("Students with a total score of 240 or more")
for student in students:
    if student['total_score'] >= 240:
        print(f"{student['name']}: {student['total_score']} points")

# 3-5 ------------

import numpy as np

data = np.random.randint(1, 101, size=100)

print(f"Data: {data}")
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Standard Deviation: {np.std(data)}")
