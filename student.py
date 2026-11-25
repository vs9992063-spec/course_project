import sys

name = sys.argv[1]
department = sys.argv[2]
semester = sys.argv[3]
course1 = sys.argv[4]
marks1 = int(sys.argv[5])
course2 = sys.argv[6]
marks2 = int(sys.argv[7])
course3 = sys.argv[8]
marks3 = int(sys.argv[9])

total = marks1 + marks2 + marks3
average = total / 3

if 90 <= average <= 100:
    grade = "S"
elif 80 <= average < 90:
    grade = "A"
elif 65 <= average < 80:
    grade = "B"
elif 50 <= average < 65:
    grade = "C"
elif 40 <= average < 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Details ---")
print("Name        :", name)
print("Department  :", department)
print("Semester    :", semester)
print(course1, ":", marks1)
print(course2, ":", marks2)
print(course3, ":", marks3)
print("Total       :", total)
print("Average     :", round(average, 2))
print("Grade       :", grade)