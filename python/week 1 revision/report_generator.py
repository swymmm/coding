#Build a Student Report Generator — one program that:

#Asks for student name and marks in 3 subjects
#Calculates total and average using arithmetic
#Prints grade (A/B/C/D/F) using if/elif/else
#Uses a loop to display results nicely
#Prints pass or fail

name=input("Enter your name: ")
sub1=float(input("Enter your marks in subject1: "))
sub2=float(input("Enter your marks in subject2: "))
sub3=float(input("Enter your marks in subject3: "))
total=sub1+sub2+sub3
avg=total/3
if avg>=90:
    grade="A"
elif avg>=80:
    grade="B"
elif avg>=70:
    grade="C"
elif avg>=60:
    grade="D"
elif avg>=50:
    grade="E"
elif avg>=40:
    grade="F"
else:
    grade="Fail"
print(f"Student Name: {name}")
print(f"Marks in Subject 1: {sub1}")
print(f"Marks in Subject 2: {sub2}")
print(f"Marks in Subject 3: {sub3}")
print(f"Total Marks: {total}")
print(f"Average Marks: {avg}")
print(f"Grade: {grade}")
if grade!="Fail":
    print("Congratulations!! You passed the exam.")
