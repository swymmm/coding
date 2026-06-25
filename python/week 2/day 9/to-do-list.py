list=[]
list.append("Wake up early")
list.append("Drink Water")
list.append("Read one book")

for i, l in enumerate(list, 1):
    print(f"{i}: {l}")

list.pop(1)

for i, l in enumerate(list, 1):
    print(f"{i}: {l}")