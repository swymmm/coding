x=10  #this is a global variable it can be accesed in this whole program

def function():
    y=5  #this is local variable only accesseble in this function
    print(x)
    print(y)


#print(y)  it will give nameError cause y is not defined outside the function
function()