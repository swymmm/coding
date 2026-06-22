def bmi_calc(weight, height):
    return weight/(height**2)
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
result=bmi_calc(weight, height)

if result<18.5:
    print("You are underweight")
elif result<25:
    print("You are normal weight")
else:
    print("You are overweight")
