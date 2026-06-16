age=int(input("enter your age: "))
if age<13:
    print("child")
elif age>=13 and age<18:
    print("teen")
elif age>=18 and age<=59:
    print("adult")
else:
    print("senior")