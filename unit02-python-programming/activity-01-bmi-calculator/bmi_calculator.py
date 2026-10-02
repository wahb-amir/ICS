''' 
 Write a program to calculate Body Mass Index (BMI).
 Ask the user for their weight (kg) and height (m)
 then compute and display their BMI and classification.
 Formula: BMI = weight / height².
 '''
 
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in M: "))

# weight ÷ height²

BMI = weight / height**2

print(f"Your BMI is {BMI:.2f}")


'''
output (example)

Enter your weight in kg: 64
Enter your height in M: 1.8                       
Your BMI is 19.75

'''
