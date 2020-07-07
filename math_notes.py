# 85-100 ➔ A (Excellent)
# 70-84 ➔ B (Good)
# 60-69 ➔ C (Medium)
# 45-59 ➔ D (Not Bad)
# 0-44 ➔ F (Failed)


math_mark = int(input('Please enter the mark: '))
if math_mark >= 85:
    print("Excellent")
elif math_mark >= 70 and math_mark < 85:
    print("Good")
elif math_mark >= 60 and math_mark < 70:
    print("Medium")
elif math_mark >= 45 and math_mark < 60:
    print("Not Bad")
else:
    print("Failed")
