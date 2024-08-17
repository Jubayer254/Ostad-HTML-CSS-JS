# BMI Calculator

# Problem Statement
# Write a program where user will give height(height) and weight(kg) and then BMI will be calculated.

# Input
# The input consists of two double numbers which are height(meter) and weight(kg).

# Output
# *if bmi < 18.5 print "Underweight" *if bmi >= 18.5 & bmi < 25.0 print "Normal weight"
# *if bmi >= 25.0 & bmi < 30.0 print "Overweight" *else print "Obese"

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter height and weight.

# Input:
# 1.6 60
# Output:
# BMI: 23.44
# Normal weight

s = input()
parts = s.split()

height = float(parts[0])
weight = float(parts[1])
bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("Normal weight")
elif bmi >= 25.0 and bmi < 30.0:
    print("Overweight")
else:
    print("Obese")