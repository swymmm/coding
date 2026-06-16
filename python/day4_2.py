marks=float(input("Enter your marks(1-100): "))
if(marks>100):
    print("Invalid marks")
elif(marks>=90 and marks<=100):
    print(f"Grade: A")
elif(marks>=80):
    print(f"Grade: B")
elif(marks>=70):
    print(f"Grade: C")
elif(marks>=60):
    print(f"Grade: D")
elif(marks>=50):
    print(f"Grade: E")
elif(marks>=40):
    print(f"Grade: F")
else:
    print("Fail")