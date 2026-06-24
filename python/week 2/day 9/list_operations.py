fruits=["apple", "banana"]

fruits.append("mango")
fruits.insert(2, "orange")
fruits.remove("banana")
#popped=fruits.pop()

fruits[0]="pineapple"

print(fruits.count("apple"))
print(fruits.index("mango"))

for f in fruits:
    print(f)