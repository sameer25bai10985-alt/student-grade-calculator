# Student Grade Calculator

print(" Student Grade Calculator ")

# Taking marks input
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Display result
print(" Result ")
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")

print("Grade:",grade)
