#Problem: Student Ranking System (Using Tuple)

#Calculate average marks of each student
#Store result as tuple → (Name, Average)
#Sort students based on highest average
#Print topper

students = (
    ("Raja", 85, 90, 88),
    ("Amit", 78, 80, 82),
    ("Neha", 92, 91, 94),
    ("Sita", 70, 75, 72)
)

result = []

# Step 1 & 2
for s in students:
    name = s[0]
    marks = s[1:]
    avg = sum(marks) / len(marks)
    result.append((name, avg))

# Step 3
sorted_result = sorted(result, key=lambda x: x[1], reverse=True)

# Step 4
topper = sorted_result[0]

print("All Averages:")
for r in sorted_result:
    print(r[0], "->", round(r[1],2))

print("\nTopper:", topper[0], "with avg:", round(topper[1],2))
