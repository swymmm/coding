cs_students={"Alice", "Bob", "Charlie", "David"}
math_students={"Charlie", "David", "Eve", "Frank"}

#union - print all students who are either in cs or math
print(cs_students | math_students)

#intersection - print all students who are in both cs and math
print(cs_students & math_students)

#difference - only in cs not in math
print(cs_students - math_students)