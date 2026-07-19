# Calculate Body Mass Index (BMI)
# Input weight (kg) and height (m), then calculate:
# BMI = weight / (height ** 2)

weight=int(input("Enter weight: "))
height=float(input("Enter height: "))
bmi=weight/(height**2)
print("BMI is: ", bmi)