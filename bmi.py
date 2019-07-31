print("Welcome to the BMI calculator!")

height = input("Insert your height in centimetres: ")
weight = input("Insert your weight in kilograms: ")

try:
    val = int(height)
    height = int(height)
except ValueError:
    print("Please use numbers to insert height!")
try:
    val = int(weight)
    weight = int(weight)
except ValueError:
    print("Please use numbers to insert weight!")

if isinstance(height, int) and isinstance(weight, int):
    height = height / 100
    bmi = weight /(height * height)

    if bmi < 18.5:
        print("Your BMI is " + str(bmi) + ". You are malnourished. Consider visiting your doctor.")
    elif bmi <= 25:
        print("Your BMI is " + str(bmi) + ". Perfect! Keep your healthy lifestyle!")
    elif bmi <= 30:
        print("Your BMI is " + str(bmi) + ". You are overweight. Consider adapting a healthier lifestyle.")
    else:
        print("your BMI is " + str(bmi) + ". You are obese. Consider visiting your doctor.")