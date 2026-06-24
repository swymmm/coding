#old way to build list
nums=[]
for n in range(1, 6):
    nums.append(n)
print(nums)

squares=[]
for i in range(1, 6):
    squares.append(i**2)

print(squares)


#same thing in one line
numbers=[i**2 for i in range(1, 6)]
print(numbers)

#with condition
evens=[i for i in range(20) if i%2==0]
print(evens)

#transform existing list
names=["swayam", "swayamm", "swym"]
upper=[n.upper() for n in names]
print(upper)