x, y=(10, 20)
print(f"x: {x}, y: {y}")

r, g, b=(255,0,0)
print(f"Red:{r}")

#swapping values
a, b=(5, 6)
a, b=b, a
print(f"a: {a}, b:{b}")

#functions returns tuples
def get_name():
    return "swayam", 22

name, age=get_name()
print(f"Name: {name}, Age: {age}")