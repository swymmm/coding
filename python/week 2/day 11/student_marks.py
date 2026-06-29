students={
    "swayam":45,
    "alok":78,
    "sachin":88,
    "shreya":95
}

highest=max(students, key=lambda x:students[x])
lowest=min(students, key=lambda x:students[x])
avg=sum(students.values())/len(students)

print("Highest marks:", highest, students[highest])
print("Lowest marks:", lowest, students[lowest])
print("Average marks:", avg)