height=float(input("enter your height in cm:"))
weight=float(input("enter your weight in kg:"))
bmi = weight / (height/100)**2
print("your BMI is:",bmi)
if bmi<=20:
    print("you are underweight")
elif bmi<=30:
    print*("you are normal")
elif bmi<=40:
    print("you are over weight")
else:
    print("you are obese")    
