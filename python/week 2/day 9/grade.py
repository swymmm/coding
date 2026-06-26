def get_grade(marks):
    if marks>=90: return"A"
    elif marks>=80: return "B"
    elif marks>=70: return "C"
    elif marks>=60: return "D"
    elif marks>=50: return "E"
    else: return "F"

marks=[44, 34, 76, 87, 45]

grades=[get_grade(m) for m in marks]

for m, g in zip(marks, grades):
    print(f"{m} : {g}")