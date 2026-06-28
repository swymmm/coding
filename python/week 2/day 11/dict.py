#dictionary has key:value pairs
student={
    "name":"swayam",
    "age":21,
    "marks":77,
    "passed":True
    }

#access by key
print(student["name"])
print(student["marks"])

#print(student["phone"])  shows key error when the key is not present


#safe option to use .get()
print(student.get("phone"))
print(student.get("phone", "Not found"))

#modifying dictionary
student["age"]=23            #update the existing
student["city"]="nipani"     # add new key:value pair
del student["passed"]        # delete the pair

print("name" in student)     # True if exists
print(len(student))          #number of key:value pairs