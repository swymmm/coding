#sets has only unique values, no duplicates
#set uses {} like dict but does not have key value pairs
set={"apple", "banana", "apple", "mango"}
print(set) # {'mango', 'banana', 'apple'}

#add or remove values
set.add("orange")
set.discard("berry") #if the "berry" is not present, it will not throw an error
set.remove("mango") #if the "mango" is not present, it will throw an error
print(set)


#check membership
print("mango" in set)
print(len(set))