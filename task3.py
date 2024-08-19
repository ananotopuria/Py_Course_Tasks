students = [
    ("Alice", 85),
    ("Bob", 78),
    ("Charlie", 92),
    ("David", 85),
    ("Eve", 78),
    ("Frank", 85),
    ("Mark", 50),
    ("George", 21)
]

unique_grades = sorted(set(score for _, score in students))
print("Unique Grades:", unique_grades)

top_performers = sorted(students, key=lambda x: x[1], reverse=True)[:3]
print("Top Performers:", [name for name, _ in top_performers])

failed_students = [(name, score) for name, score in students if score < 51]
print("Failed Students:", failed_students)
