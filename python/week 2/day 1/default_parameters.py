def greet(name, msg="Good Morning!!"): #good morning is a default 
    print(f"{msg} {name}")

greet("swayam")
greet("swayam", "Good Evening!!")  #we used different word

#default parameter should come last

def power(base, exp=2):
    return base**exp

print(power(2))
print(power(2, 10))