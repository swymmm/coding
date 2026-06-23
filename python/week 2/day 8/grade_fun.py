def get_grade(marks):
    if marks>=90: return"A"
    elif marks>=80: return "B"
    elif marks>=70: return "C"
    elif marks>=60: return "D"
    elif marks>=50: return "E"
    else: return "F"

def is_pass(marks):
    return marks>=40

scores=[44, 34, 76, 87, 45]
for s in scores:
    grade= get_grade(s)
    status="Pass" if is_pass(s) else "Fail"
    print(f"{s} : {grade} : {status}")