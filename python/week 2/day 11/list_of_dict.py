#Each student is a dict. Store them in a list
students=[
    {"name":"swayam","marks":77},
    {"name":"sachin","marks":88},
    {"name":"shreya","marks":95}
]

#print all students
for s in students:
    print(f"{s['name']} : {s['marks']}")

#print top student
top=max(students, key= lambda s:s["marks"])
print(f"Top student is {top['name']} with marks {top['marks']}")